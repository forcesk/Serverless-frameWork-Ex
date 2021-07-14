import json
import os
import requests
from get_token import get_token
from verify_token import verify_token

def authorizerFunc(event, context):

    id = 1
    token = get_token(event)

    # Token vacio, no hay JWT, acceso denegado
    if token == 0:
        id = 2
        policy = generate_policy(id,'Deny',event['methodArn'])
        return policy

    #print('JWT: '+str(token))
    #print('\n')

    verify_token(token)

    if id == 1 :
        policy = generate_policy(id,'Allow',event['methodArn'])
        return policy

    else:
        policy = generate_policy(id,'Deny',event['methodArn'])
        return policy

def generate_policy(principal_id, effect,resource, scopes=None):
    policy = {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2021-07-13',
            'Statement': [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": resource
                }
            ]
        }
    }
    return policy
