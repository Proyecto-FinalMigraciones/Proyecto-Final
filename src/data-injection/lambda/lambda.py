import http.client
from functions import obtener_datos
from constant import todos_los_indicadores

def handler(event, context):
    print("🐍 File: lambda/lambda.py | Line: 4 | undefined ~ event",event)
    for indicador in todos_los_indicadores:
        obtener_datos(indicador)
    return
