import json


def hello(event, context):
    body = {
        "message": "Hello there!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


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

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
