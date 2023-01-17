import mercadopago
import os
import json

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    body = json.loads(event["body"])

    pago = {
        "transaction_amount": float(body["transaction_amount"]),
        "token": body["token"],
        "description": body["description"],
        "installments": int(body["installments"]),
        "payment_method_id": body["payment_method_id"],
        "issuer_id": body["issuer_id"],
        "payer": {
            "email": body["payer"]["email"],
            "identification": {
                "type": body["payer"]["identification"]["type"],
                "number": body["payer"]["identification"]["number"],
            }
        }
    }
    
    pago_response = sdk.payment().create(payment_data)
    pago = pago_response["response"]
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "http://localhost:3000/",
        },
        "body": json.dumps(pago),
    }

# payment_data = {
#     "transaction_amount": float(request.POST.get("transaction_amount")),
#     "token": request.POST.get("token"),
#     "description": request.POST.get("description"),
#     "installments": int(request.POST.get("installments")),
#     "payment_method_id": request.POST.get("payment_method_id"),
#     "payer": {
#         "email": request.POST.get("cardholderEmail"),
#         "identification": {
#             "type": request.POST.get("identificationType"),
#             "number": request.POST.get("identificationNumber"),
#         },
#         "first_name": request.POST.get("cardholderName"),
#     }
# }

# payment_response = sdk.payment().create(payment_data)
# payment = payment_response["response"]

# print(payment)
