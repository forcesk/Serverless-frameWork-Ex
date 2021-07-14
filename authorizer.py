import json
import os
import requests
from get_token import get_token

def authorizerFunc(event, context):

    id = 1
    token = get_token(event)
    print('Token value: '+str(event))

    if token == 0:
        id = 2


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
