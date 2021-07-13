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
        "message": "Private test!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    
