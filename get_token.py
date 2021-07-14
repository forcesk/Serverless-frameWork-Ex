def get_token(event):

    whole_auth_token = event.get('authorizationToken')

    ## Token vacio
    if not whole_auth_token :
        print("ERROR DEBIDO A TOKEN INVÁLIDO.")
        return 0

    token_parts = whole_auth_token.split(' ')
    auth_token = token_parts[1]

    ## Parte bearer
    token_method = token_parts[0]

    # Token no válido
    if not (token_method.lower() == 'bearer' and auth_token):
        print("ERROR DEBIDO A JWT INVÁLIDO.")
        return 0

    #Se regresa el JWT
    return auth_token
