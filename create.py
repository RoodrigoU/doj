import requests

url = "https://api.culqi.com/v2/orders"

payload = {
            "amount": 53*100,
            "currency_code": "USD",
            "description": "Taller Python de Cero a Ninja",
            "order_number": "pedido-929d9d912",
            "client_details": {
              "first_name":"erick",
              "email": "lifehack.py@gmail.com",
                  "phone_number": "+51991244662"
            },
           "expiration_date": 1574985600
       }

headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer sk_test_P92zyYskVlMZ3KqD",
    }

response = requests.post(url, json=payload, headers=headers)

print(response.text)
