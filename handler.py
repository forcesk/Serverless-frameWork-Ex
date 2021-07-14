import json
from DB_manager import insertDB

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

    # Se inserta 'Acceso Concendido' en la tabla items de test.db
    insertDB()

    body = {
        "message": "Acceso Concedido, nuevo dato agregado a la base de datos."
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
