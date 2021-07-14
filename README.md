# Ejercicio con Serverless Framework

## Librerías
* [Serverless Offline](https://www.serverless.com/plugins/serverless-offline)
* [PyJWT](https://pyjwt.readthedocs.io/en/latest/)
* [Sqlite](https://www.sqlite.org/index.html)

## Recursos
* [jwt.io](https://jwt.io)
* [Serverless Docs](https://www.serverless.com/plugins/serverless-offline)
* [Lambda authorizer docs](https://www.serverless.com/learn/tutorial/aws-lambda-authorizers-frontend-setup)
* [Lambda authorizer AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)
* [Postman](https://www.postman.com)

## Modo de uso
```
serverless offline --noPrependStageInUrl --httpPort 3119 --lambdaPort 6057
```
> El puerto http y lambda son solo para no crear conflictos de puertos ocupados :thumbsup: , la opción no Prepend quita el 'stage' de la URL.

En las primeras versiones corria en AWS :earth_americas: , pero debido a los requirimientos ahora trabaja con Serverless Offline.

Para comprobar su funcionamiento se usó Postman.

### El código JWT correcto
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwicm9sZSI6ImJvdCIsImFjY2Vzc0tleSI6IlFXRVJUWVVJT1AiLCJpYXQiOjE1MTYyMzkwMjJ9.VjEN_JL8qAUxYtE5H11r3_CoAaBIRqGKJ1VQo9iwPgI

```

### El código obedece al siguiente diagrama:
![alt text](https://github.com/forcesk/Serverless-frameWork-Ex/blob/a2333ee0694e5df0eb36996bddca6cc1dc2e6ffd/images/diagram.png) 
  


