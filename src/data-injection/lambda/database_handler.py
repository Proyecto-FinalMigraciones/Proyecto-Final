import os
import pymysql
import pandas as pd

class DatabaseHandler:
    def __init__(self):
        db_host = os.environ["DB_HOST"]
        db_user = os.environ["DB_USER"]
        db_password = os.environ["DB_PASSWORD"]
        db_name = os.environ["DB_NAME"]

        self.connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

    def insert_dataframe(self, dataframe, table_name):
        try:
            columns = ', '.join([f'`{column}`' for column in dataframe.columns])

            with self.connection.cursor() as cursor:
                for index, row in dataframe.iterrows():
                        
                        pais = row['Pais']
                        año = row['Año']
                
                        # Consulta SQL para verificar si ya existe un registro con los mismos valores de 'Pais' y 'Año'
                        select_query = f"SELECT 1 FROM `{table_name}` WHERE `Pais` = %s AND `Año` = %s"
                        cursor.execute(select_query, (pais, año))
                        existe_registro = cursor.fetchone()

                        if not existe_registro:
                            values_str = ', '.join([f'{str(value)}' for value in row])
                            values_list = values_str.split(', ')
                            query = f"INSERT INTO `{table_name}` ({columns}) VALUES ({', '.join(['%s' for _ in values_list])})"
                            cursor.execute(query, values_list)
                        

            self.connection.commit()
        except Exception as e:
            print(f"Error al insertar datos en MySQL: {str(e)}")


    def close_connection(self):
        self.connection.close()
