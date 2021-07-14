import json

def public(event, context):
    body = {
        "message": "Hello World!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def private(event, context):
    body = {
        "message": "Acceso Concedido."
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
