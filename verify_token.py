import os
import json
import base64

from six.moves.urllib.request import urlopen
import jwt

def verify_token(token):


    jwt_options = {
        'verify_signature': False,
        'verify_exp': True,
        'verify_nbf': False,
        'verify_iat': True,
        'verify_aud': False
    }

    print("secret \n")
    jwt.decode(
    token,"",algorithms=['HS256'],options=jwt_options
)
