import http.client
import pandas as pd
import os
import mysql.connector
from sqlalchemy import create_engine
from functions import obtener_datos
from constant import todos_los_indicadores

def handler(event, context):
    # print("🐍 File: lambda/lambda.py | Line: 4 | undefined ~ event",event)


    # indicadores = pd.DataFrame()

    dataframes = {}  # Un diccionario para almacenar los DataFrames

    for indicador in todos_los_indicadores:
      dataframe = obtener_datos(indicador)
      dataframe = dataframe.drop(columns=['unit', 'obs_status', 'decimal', 'indicator'])
      dataframe = dataframe.rename(columns={'value': indicador})
      dataframe['country'] = dataframe['country'].apply(lambda x: x['value'])
        
      # Almacena el DataFrame en el diccionario usando el nombre del indicador como clave
      dataframes[indicador] = dataframe


    output_dataframe = dataframes[list(dataframes.keys())[0]]

    # Realiza el merge con los demás DataFrames
    for indicador, dataframe in dataframes.items():
      if indicador != list(dataframes.keys())[0]:
        output_dataframe = output_dataframe.merge(
            dataframe,
            on=['country','countryiso3code', 'date'],
            how='inner',
            # suffixes=('', f'_{indicador.replace(".", "_")}')  # Agrega sufijos
        )
    


    # conexión de SQLAlchemy
    conexion = create_engine('mysql+mysqlconnector://admin:migration2023@database-migration.cq1xp27nrjmz.us-east-2.rds.amazonaws.com:3306/migration')

    try:
        # Carga el DataFrame en una tabla existente o crea una nueva tabla
        output_dataframe.to_sql(name="prueba", con=conexion, if_exists="replace", index=False)

    except Exception as e:
        print(f"Error al cargar datos en MySQL: {str(e)}")
        
