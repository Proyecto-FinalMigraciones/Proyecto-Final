from sqlalchemy import create_engine
import pandas as pd
import mysql.connector
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

conexion = create_engine('mysql+mysqlconnector://admin:migration2023@database-migration.cq1xp27nrjmz.us-east-2.rds.amazonaws.com:3306/migration')

carga_inicial = [
     {
        'csv': pd.read_csv(os.path.join(current_dir, 'Datasets', 'migracion_neta.csv')),
        'name': 'migracion_neta'
    },
     {
        'csv': pd.read_csv(os.path.join(current_dir, 'Datasets', 'refugee-population-by-country-or-territory-of-origin.csv')),
        'name': 'refugiados_pais_origen'
    },
     {
        'csv': pd.read_csv(os.path.join(current_dir, 'Datasets', 'refugee-population-by-country-or-territory-of-asylum.csv')),
        'name': 'refugiados_pais_asilo'
    },
     {
        'csv': pd.read_csv(os.path.join(current_dir, 'Datasets', 'destino_H_M.csv')),
        'name': 'migracion_pais_destino'
    },
     {
        'csv': pd.read_csv(os.path.join(current_dir, 'Datasets', 'indicadoresmigracion.csv')),
        'name': 'indicadores'
    },
     {
        'csv': pd.read_csv(os.path.join(current_dir, 'Datasets', 'mujeres_Origen_Destino.csv')),
        'name': 'migrantes_mujeres'
    },
     {
        'csv': pd.read_csv(os.path.join(current_dir, 'Datasets', 'origen_H_M.csv')),
        'name': 'migracion_pais_origen'
    },
     {
        'csv': pd.read_csv(os.path.join(current_dir, 'Datasets','poblacion_H_M.csv')),
        'name': 'poblacion_H_M'
    },
     {
        'csv': pd.read_csv(os.path.join(current_dir, 'Datasets','incidentes.csv')),
        'name': 'incidentes'
    }
]

def procesar_carga_inicial(lista):
    for dataset in lista:
        ds = dataset['csv']
        ds.to_sql(name=dataset['name'], con=conexion, if_exists='replace', index=False)
    return

procesar_carga_inicial(carga_inicial)

conexion.dispose()