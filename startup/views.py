from django.shortcuts import render
from .models import ModelContact, ModelPayment, ModelPagoEfectivo
from django.http import JsonResponse
import culqipy
from uuid import uuid4
import logzero
from logzero import logger
import datetime
import requests
from modules.detect_currency_country import *

logzero.logfile("/tmp/django.log", maxBytes=1e6, backupCount=3)
culqipy.public_key = 'pk_test_QfmMu2RtRgv6TEtg'
culqipy.secret_key = 'sk_test_P92zyYskVlMZ3KqD'
MOUNT_TALLER_PYTHON = 120

def create_payment_checkout(token_culqi, token_ecommerce, email, monto, item_title, name, lastname, phone):
    dir_charge = {
        'amount': monto,
        'capture': True,
        'country_code': 'PE',
        'currency_code': 'PEN',
        'description': item_title,
        'installments': 0,
        'metadata': {'client_id': token_ecommerce},
        'email': email,
        'source_id': token_culqi
                   }
    status_object, code, type_ = '', '', ''
    # obj = culqipy.Token.get(TOKEN_ID)
    obj = culqipy.Charge.create(dir_charge)
    status_object = obj.get('object', '')
    amount = obj.get('amount', 0.0)
    if amount:
        amount = float(amount)/100
    charge_id = obj.get('id', '')
    type_ = obj.get('outcome', '')
    if type_:
        type_ = type_.get('type', '')
    code = obj.get('outcome', '')
    if code:
        code = code.get('code', '')
    reference_code = obj.get('reference_code', '')
    authorization_code = obj.get('authorization_code', '')
    merchant_message = obj.get('outcome', '')
    if merchant_message:
        merchant_message = merchant_message.get('merchant_message', '')
    ModelPayment.objects.create(
                                    status_object=status_object,
                                    amount=amount,
                                    charge_id=charge_id,
                                    type=type_,
                                    code=code,
                                    reference_code=reference_code,
                                    authorization_code=authorization_code,
                                    merchant_message=merchant_message,
                                    email=email,
                                    data_payment=obj,
                                    name=name,
                                    lastname=lastname,
                                    phone=phone
                                )

    if status_object == 'charge' and (type_ == 'venta_exitosa' or code == 'AUT0000'):
        return True
    else:
        return False

def create_payment_pagoefectivo(mount, first_name, last_name, email, phone):
    try:
        url = "https://api.culqi.com/v2/orders"
        time_max = datetime.datetime.now() + datetime.timedelta(days=7)
        expiration_date_timestamp = datetime.datetime.timestamp(time_max)
        order_number = 'pedido-{}'.format(str(expiration_date_timestamp).split('.')[0])
        payload = {
                    "amount": MOUNT_TALLER_PYTHON*100,
                    "currency_code": "PEN",
                    "description": "Taller de Python",
                    "order_number": order_number,
                    "client_details": {
                      "first_name": first_name,
                      "last_name": last_name,
                      "email": email,
                      "phone_number": phone
                    },
                   "expiration_date": expiration_date_timestamp
               }
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer {}".format(culqipy.secret_key)
            }
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        return response.json()
    except Exception as e:
        print(e)
        return False


# Create your views here.
def home(request):
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except Exception as e:
        pass
    if mobile:
        uri_whatsapp = 'api'
    else:
        uri_whatsapp = 'web'
    return render(request, 'base.html', {'uri_whatsapp': uri_whatsapp})


def contact(request):
    name = request.POST.get('username', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    ModelContact.objects.get_or_create(name=name, email=email, phone=phone)
    return JsonResponse({'status': 'ok'})


def checkout(request):
    mount, simbol, country_code = get_mount_for_county(request)
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_whatsapp = 'api'
    else:
        uri_whatsapp = 'web'

    if request.method == "POST":
        NameComplete = request.POST.get('NameComplete', '')
        NameComplete = NameComplete.split(' ', 1)
        if len(NameComplete) == 2:
            firstName = NameComplete[0]
            lastName = NameComplete[1]
        else:
            firstName = NameComplete[0]
            lastName = NameComplete[0]

        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        if request.POST.get('type_payment', '') == 'pago_efectivo':
            print('pago_efectivo',mount,
            firstName,
            lastName,
            email,
            phone)
            obj_pay = create_payment_pagoefectivo(
                    mount,
                    firstName,
                    lastName,
                    email,
                    phone
                    )
            if obj_pay:
                print(obj_pay)
                ModelPagoEfectivo.objects.create(
                            object=obj_pay.get('object', ''),
                            create_data_time=obj_pay.get('creation_date', 0),
                            expiration_date_time=obj_pay.get('expiration_date', 0),
                            orde_id=obj_pay.get('id', ''),
                            order_number=obj_pay.get('order_number', ''),
                            amount=obj_pay.get('amount', 0),
                            payment_code=obj_pay.get('payment_code', ''),
                            currency_code=obj_pay.get('currency_code', ''),
                            description=obj_pay.get('description', ''),
                            state=obj_pay.get('state', ''),
                            total_fee=obj_pay.get('total_fee', ''),
                            net_amount=obj_pay.get('net_amount', ''),
                            fee_details=obj_pay.get('fee_details', ''),
                            updated_at=obj_pay.get('updated_at', ''),
                            paid_at=obj_pay.get('paid_at', ''),
                            available_on=obj_pay.get('available_on', ''),
                            firstname=firstName,
                            lastname=lastName,
                            phone=phone,
                            email=email,
                            data_payment=obj_pay
                )
                return JsonResponse({'status': True, 'codigo_cip': obj_pay.get('payment_code', '')})
            else:
                return JsonResponse({'status': False, 'message': 'En mantenimiento, intentalo luego.'})

        elif request.POST.get('type_payment', '') == 'pago_tarjeta':
            token_payment_gateway = request.POST.get('token_payment_gateway', '')
            tk_django = request.POST.get('tk_django', '')
            print(firstName, lastName, token_payment_gateway, tk_django)

            checkout_validate = create_payment_checkout(
                    token_payment_gateway,
                    tk_django,
                    email,
                    MOUNT_TALLER_PYTHON*100, # verificar! enviar en centimos
                    'Taller Python',
                    firstName,
                    lastName,
                    phone
                )
            if checkout_validate:
                return JsonResponse({'token_active': True})
            else:
                return JsonResponse({'token_active': False})
    else:
        return render(
                request, 'checkout.html',
                {'uri_whatsapp': uri_whatsapp,
                'tk_django': str(uuid4()),
                'mount': mount,
                 'simbol': simbol,
                 'country_flag': country_code.lower()}
            )


def checkoutSuccesss(request):
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except Exception as e:
        pass
    if mobile:
        uri_whatsapp = 'api'
    else:
        uri_whatsapp = 'web'
    return render(
            request, 'checkout_success.html',
            {'uri_whatsapp': uri_whatsapp}
        )


def webhook(request):
    if request.method == "POST":
        r_post = request.POST
        r_body = request.body
        logger.info(str(r_post))
        logger.info(str(r_body))
        return JsonResponse({'response': 'Webhook de Culqi recibido'})
