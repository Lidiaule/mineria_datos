'''Ej5c: Elimina con DELETE las filas del ticker BBVA. Muestra las filas antes y
después.'''

from pyspark.sql.functions import col
from src.modelo.configuracion.Configuracion import RUTA_BRONZE_IBEX
from src.modelo.funciones.AlmacenamientoDatos import leer_delta
from src.modelo.funciones.OperacionesDelta import eliminar_filas


class Ejercicio5C:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 5.c")

        # Comprobamos las filas de BBVA antes
        print("Filas de BBVA antes del DELETE:")
        leer_delta(self.spark, RUTA_BRONZE_IBEX).filter(col("Ticker") == "BBVA.MC").show(truncate=False)

        # Eliminamos todas las filas del ticker BBVA
        eliminar_filas(self.spark, RUTA_BRONZE_IBEX, "Ticker = 'BBVA.MC'")

        # Mostramos las filas despues
        print("Filas de BBVA despues del DELETE:")
        leer_delta(self.spark, RUTA_BRONZE_IBEX).filter(col("Ticker") == "BBVA.MC").show(truncate=False)
