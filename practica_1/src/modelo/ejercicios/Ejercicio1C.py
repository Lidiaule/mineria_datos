'''Ej1c (opcional): Lee de vuelta el Parquet que acabas de escribir y muestra el
esquema y las 5 primeras filas. A continuación, lee solo las columnas Ticker, Date
y Close (column pruning) y muéstralas. Comenta qué ventaja tiene leer solo esas
columnas frente a leerlas todas.'''

from src.modelo.configuracion.Configuracion import RUTA_BRONZE_IBEX
from src.modelo.funciones.AlmacenamientoDatos import leer_parquet


class Ejercicio1C:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 1.c")

        # Volvemos a leer el Parquet 
        df = leer_parquet(self.spark, RUTA_BRONZE_IBEX)

        df.printSchema()
        df.show(5, truncate=False)

        # Leemos solo Ticker, Date y Close
        df_reducido = leer_parquet(self.spark, RUTA_BRONZE_IBEX).select("Ticker", "Date", "Close")

        df_reducido.show(5, truncate=False)

        # Ventaja:
        print("Leer solo Ticker, Date y Close reduce el input y output porque Parquet puede leer unicamente esas columnas")

        return df
