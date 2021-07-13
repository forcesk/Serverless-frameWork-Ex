import json

def authorizerFunc(event, context):
    body = {
        "message": "Hello there!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
