import pandas as pd
from functions import transformacion
from constant import todos_los_indicadores
from database_handler import DatabaseHandler

def handler(event, context):
  try:
    db_handler = DatabaseHandler()
    indicadores_df = transformacion(todos_los_indicadores)
    db_handler.insert_dataframe(indicadores_df, "prueba")
    db_handler.close_connection()
  except Exception as e:
      print(f"Error en la funcion general: {str(e)}")
