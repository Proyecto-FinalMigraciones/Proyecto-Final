import http.client
import json
import pandas as pd


def obtener_paginas_totales(indicador): 

    host = "api.worldbank.org"
    path = f"/v2/country/all/indicator/{indicador}?format=json&date=2000:2020"

    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path)

    response = conn.getresponse()
    data = response.read()

    json_data = json.loads(data)
    conn.close()
    # Obtiene el valor de "pages" en una variable
    total_pages = json_data[0]["pages"]
    return total_pages
   

def obtener_datos(indicador):

    total_data = []
    paginas_totales = obtener_paginas_totales(indicador)
    host = "api.worldbank.org"
    conn = http.client.HTTPSConnection(host)

    for pagina in range(1, paginas_totales + 1):
        try:
            path = f"/v2/country/all/indicator/{indicador}?format=json&date=2000:2020&page={pagina}"
            conn.request("GET", path)
            response = conn.getresponse()
            data = response.read()
            json_data = json.loads(data)

            if len(json_data) >= 2 and isinstance(json_data[1], list):
               total_data.extend(json_data[1])
            
        except Exception as e:
            print(f"🐍 File: lambda/functions.py | Line: 31 | obtener_datos ~ Error en página {pagina}: {str(e)}")


    data_df = pd.DataFrame(total_data)
    return data_df

 