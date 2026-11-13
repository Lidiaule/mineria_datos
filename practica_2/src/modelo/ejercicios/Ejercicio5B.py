'''Ej5b: Repite la escritura del ejercicio anterior con option("mergeSchema", "true") y
comprueba si sigue rechazándolo.'''

from pyspark.sql.functions import col

from src.modelo.configuracion.Configuracion import RUTA_BRONZE_IBEX
from src.modelo.funciones.AlmacenamientoDatos import leer_delta, guardar_delta

class Ejercicio5B:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 5.b")

        # Volvemos a crear la columna nueva
        df_nuevo = leer_delta(self.spark, RUTA_BRONZE_IBEX).withColumn("Close_mas5", col("Close") + 5)

        # Utilizamos mergeSchema.
        guardar_delta(df_nuevo, RUTA_BRONZE_IBEX, modo="append", merge_schema=True)

        # Mostramos el esquema para comprobar que la nueva columna existe.
        leer_delta(self.spark, RUTA_BRONZE_IBEX).printSchema()
