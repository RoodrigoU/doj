import requests

url = "https://api.culqi.com/v2/orders"

payload = {
            "amount": 53*100,
            "currency_code": "USD",
            "description": "Taller Python de Cero a Ninja",
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
