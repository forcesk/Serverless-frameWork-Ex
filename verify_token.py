import json
import jwt

def verify_token(token):

    #Opciones de Verificación
    jwt_options = {
        'verify_signature': False,
        'verify_exp': True,
        'verify_nbf': False,
        'verify_iat': True,
        'verify_aud': False
    }

    #Datos del JWT
    try:
        payload = jwt.decode(token,algorithms=['HS256'],options=jwt_options)

    except:
        print("\n Error en el Token JWT \n")
        return False


    #print(payload['role'])
    #print(payload['accessKey'])

    #Se comprueba si contiene los datos correctos
    if payload['role']=="bot" and payload['accessKey']=="QWERTYUIOP":
        print("\n Acceso concedido. \n")
        return True

    # Si NO contiene los datos correctos
    else:
        print("\n Acceso DENEGADO. \n")
        return False
