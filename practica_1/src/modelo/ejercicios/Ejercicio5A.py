'''Ej5a: Crea una columna nueva, con los datos de la columna close y sumale 5
(nombre de la columna Close_mas5). Intenta escribir la tabla con esa columna de
más en modo append y comprueba que Delta lo rechaza (error de esquema).'''

from pyspark.sql.functions import col

from src.modelo.configuracion.Configuracion import RUTA_BRONZE_IBEX
from src.modelo.funciones.AlmacenamientoDatos import leer_delta, guardar_delta
from src.modelo.funciones.OperacionesDelta import obtener_version_actual


class Ejercicio5A:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 5.a")

        # Guardamos la version anterior 
        version_antes_5a = obtener_version_actual(self.spark, RUTA_BRONZE_IBEX)

        # Creamos nueva columna y sumamos 5
        df_nuevo = leer_delta(self.spark, RUTA_BRONZE_IBEX).withColumn("Close_mas5", col("Close") + 5)

        # Hacemos el append y comprobamos
        try:
            guardar_delta(df_nuevo, RUTA_BRONZE_IBEX, modo="append", merge_schema=False)
            print("La escritura no ha sido rechazada")

        except Exception as e:
            print("Delta rechaza la escritura porque Close_mas5 no coincide con el esquema actual de la tabla")
            print(str(e))

        return version_antes_5a
