import mysql.connector # Importa el conector de MySQL (API de Python)

#Clase para la conexion a la base de datos para ejecutar consultas
class conexion:
    def __init__(self):
        self.__conn = mysql.connector.connect(
            host='localhost',
            user='sistemas',
            password='sisT2025',
            database='banco'
        )
#Metodo para consultar las tablas de la base de datos y probar la conexion a. Consultar
    def probar_conexion(self):
        cursor = self.__conn.cursor()
        cursor.execute("SHOW TABLES")
        for table in cursor:
            print(table)
        cursor.close()
        self.__conn.close()

conexion = conexion() # Crear una instancia de la clase conexion
conexion.probar_conexion() # Probar la conexion a la base de datos


