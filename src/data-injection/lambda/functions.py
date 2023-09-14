import http.client
import json
import pandas as pd
import datetime
import os
import pymysql

def obtener_paginas_totales(indicador): 

    año_actual = datetime.date.today().year
    host = "api.worldbank.org"
    path = f"/v2/country/all/indicator/{indicador}?format=json&date=2020:{año_actual}"

    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path)

    response = conn.getresponse()
    data = response.read()

    json_data = json.loads(data)
    conn.close()
    # Obtiene el valor de "pages" en una variable
    paginas_totales = json_data[0]["pages"]
    return paginas_totales
   

def obtener_datos(indicador):

    total_data = []
    paginas_totales = obtener_paginas_totales(indicador)
    # paginas_totales = 3
    host = "api.worldbank.org"
    conn = http.client.HTTPSConnection(host)

    for pagina in range(1, paginas_totales + 1):
        try:
            año_actual = datetime.date.today().year
            path = f"/v2/country/all/indicator/{indicador}?format=json&date=2020:{año_actual}&page={pagina}"
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

def transformacion(parametro):
    dataframes = {}  # Almacena los dataframe individuales de cada indicador

    for indicador in parametro:
      dataframe = obtener_datos(indicador)
      dataframe = dataframe.drop(columns=['unit', 'obs_status', 'decimal', 'indicator'])
      dataframe = dataframe.rename(columns={'value': indicador})
      dataframe['country'] = dataframe['country'].apply(lambda x: x['value'])
      dataframes[indicador] = dataframe

    dataframe_final = dataframes[list(dataframes.keys())[0]]

    for indicador, dataframe in dataframes.items():
      if indicador != list(dataframes.keys())[0]:
        dataframe_final = dataframe_final.merge(
            dataframe,
            on=['country','countryiso3code', 'date'],
            how='inner',
        )

    dataframe_final = dataframe_final.rename(columns={
    'date': 'Año',
    'country': 'Pais',
    'countryiso3code': 'Id_Pais',
    'NY.GDP.MKTP.KD.ZG': 'Crecimiento_PIB',
    'SL.UEM.TOTL.ZS': 'Tasa_desempleo',
    'NY.GDP.DEFL.KD.ZG': 'Inflacion_PIB',
    'VC.IHR.PSRC.P5': 'Homicidios_intencionales',
    'VC.BTL.DETH': 'Muertes_Conflicto',
    'CC.PER.RNK': 'Control_Corrupcion',
    'EN.ATM.CO2E.KT': 'Emisiones_CO2',
    'SP.DYN.LE00.IN': 'Esperanza_vida',
    'SM.POP.NETM': 'Migracion_neta',
    'SP.POP.TOTL': 'Poblacion_total',
    # 'SP.POP.TOTL': 'Poblacion_total',
    # 'SP.POP.TOTL.MA.IN': 'Poblacion_masculina',
    # 'SP.POP.TOTL.FE.IN': 'Poblacion_femenina',
    })



    return dataframe_final
