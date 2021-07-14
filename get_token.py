def get_token(event):
    # whole_auth_token should look like:
    # "Bearer SOME_CODE_GIBBERISH6r712fyasd.othergibberish.finalgibberish"

    whole_auth_token = event.get('authorizationToken')

    ## Token vacio
    if not whole_auth_token :
        print("ERROR DEBIDO A TOKEN INVÁLIDO.")
        return 0


    print('Client token: ' + whole_auth_token)
    print('Method ARN: ' + event['methodArn'])
    print("Equis \n")

    token_parts = whole_auth_token.split(' ')
    auth_token = token_parts[1]

    #print('Auth_token:  '+str(auth_token))
    #print('\n')

    ## Parte bearer
    token_method = token_parts[0]

    # Token no válido
    if not (token_method.lower() == 'bearer' and auth_token):
        print("ERROR DEBIDO A JWT INVÁLIDO.")
        return 0

    # At this point we've confirmed the token format looks ok
    # So return the unverified token
    return auth_token
