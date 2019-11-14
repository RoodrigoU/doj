from django.shortcuts import render
from .models import ModelContact, ModelPayment
from django.http import JsonResponse
import culqipy
from uuid import uuid4

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
                                    lastname=lastname
                                )

    if status_object == 'charge' and (type_ == 'venta_exitosa' or code == 'AUT0000'):
        return True
    else:
        return False


# Create your views here.
def home(request):
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except Exception as e:
        pass
    if mobile:
        uri_whatsapp = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20Quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20taller."
    else:
        uri_whatsapp = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20Quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20taller."
    return render(request, 'base.html', {'uri_whatsapp': uri_whatsapp})


def contact(request):
    name = request.POST.get('username', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    ModelContact.objects.get_or_create(name=name, email=email, phone=phone)
    return JsonResponse({'status': 'ok'})


def checkout(request):
    firstName = request.POST.get('firstName', '')
    lastName = request.POST.get('lastName', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    token_payment_gateway = request.POST.get('token_payment_gateway', '')
    tk_django = request.POST.get('tk_django', '')
    print(firstName, lastName, token_payment_gateway, tk_django)
    mobile = False
    try:
        mobile = request.user_agent.is_mobile
    except:
        pass
    if mobile:
        uri_whatsapp = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20Quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20taller."
    else:
        uri_whatsapp = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20Quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20taller."

    if request.method == "POST":
        checkout_validate = create_payment_checkout(
                token_payment_gateway,
                tk_django,
                email,
                180*100, # verificar! enviar en centimos
                'Taller Python de Cero a Ninja',
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
        uri_whatsapp = "https://api.whatsapp.com/send?phone=51935489552&text=Hola%21%20Quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20taller."
    else:
        uri_whatsapp = "https://web.whatsapp.com/send?phone=51935489552&text=Hola%21%20Quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20el%20taller."

    return render(
            request, 'checkout_success.html',
            {'uri_whatsapp': uri_whatsapp}
        )
