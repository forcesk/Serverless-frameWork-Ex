import json
from get_token import get_token
from verify_token import verify_token

def AUTHORIZER(event, context):

    # principal_id
    id = 'Private_test'

    token = get_token(event)

    # Token vacio, no hay JWT, acceso denegado
    if token == 0:
        policy = generate_policy(id,'Deny',event['methodArn'])
        return policy

    # Verificación de datos en el Token
    flag = verify_token(token)

    # Credenciales correctas del JWT
    if flag:
        policy = generate_policy(id,'Allow',event['methodArn'])
        return policy

    #Credenciales incorrectas, acceso denegado.
    else:
        policy = generate_policy(id,'Deny',event['methodArn'])
        return policy

# Función que genera la politica de acceso.
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
