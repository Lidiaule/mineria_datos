'''Ej8: Construye la capa silver. Limpia la base de datos sentimiento y guárdalo en
data/lake/silver/sentimiento. Los sectores del CSV están en español. Justifica la
construcción/modificación de los datos en el pdf. Muestra cuántas filas tiene
cada tabla.'''


# Use IA para ayudarme a plantear y organizar la limpieza de datos de sentimiento
from src.modelo.configuracion.Configuracion import (RUTA_BRONZE_SENTIMIENTO, RUTA_SILVER_SENTIMIENTO)
from src.modelo.funciones.AlmacenamientoDatos import leer_delta, guardar_delta
from src.modelo.funciones.LimpiezaDatos import limpiar_sentimiento


class Ejercicio8:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 8")

        # Leemos el sentimiento crudo de bronze
        df_bronze = leer_delta(self.spark, RUTA_BRONZE_SENTIMIENTO)

        # Aplicamos la limpieza para pasar a silver
        df_silver = limpiar_sentimiento(df_bronze)

        # Guardamos el resultado limpio en silver
        guardar_delta(df_silver, RUTA_SILVER_SENTIMIENTO, "overwrite")

        # Mostramos las filas de cada tabla
        print(f"Filas sentimiento bronze: {df_bronze.count()}")
        print(f"Filas sentimiento silver: {df_silver.count()}")

        return df_silver
