from django.shortcuts import render
from .models import ModelContact, ModelPayment
from django.http import JsonResponse
import culqipy
from uuid import uuid4
import logzero
from logzero import logger

logzero.logfile("/tmp/django.log", maxBytes=1e6, backupCount=3)
culqipy.public_key = 'pk_test_QfmMu2RtRgv6TEtg'
culqipy.secret_key = 'sk_test_P92zyYskVlMZ3KqD'


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

def create_payment_pagoefectivo():
    url = "https://api.culqi.com/v2/orders"
    payload = {
                "amount": 53*100,
                "currency_code": "USD",
                "description": "Taller de Python",
                "order_number": "pedido-99d9d9",
                "client_details": {
                  "first_name":"erick",
                  "last_name": "conde",
                  "email": "lifehack.py@gmail.com",
                  "phone_number": "+51945145288"
                },
               "expiration_date": 1574208000
           }
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer sk_test_P92zyYskVlMZ3KqD",
        }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)



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
        if request.POST.get('type_payment', '') == 'pago_efectivo':
            pass
        elif request.POST.get('type_payment', '') == 'pago_tarjeta':
            firstName = request.POST.get('firstName', '')
            lastName = request.POST.get('lastName', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            token_payment_gateway = request.POST.get('token_payment_gateway', '')
            tk_django = request.POST.get('tk_django', '')
            print(firstName, lastName, token_payment_gateway, tk_django)

            checkout_validate = create_payment_checkout(
                    token_payment_gateway,
                    tk_django,
                    email,
                    169*100, # verificar! enviar en centimos
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
                'tk_django': str(uuid4())}
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
