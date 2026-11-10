'''Ej2c (opcional): Vuelve a ejecutar la carga del Ej2b pero esta vez en modo append.
Cuenta las filas de la carpeta antes y después y comprueba que pasa. Comenta que
ocurre. '''

from src.modelo.configuracion.Configuracion import RUTA_BRONZE_SENTIMIENTO
from src.modelo.funciones.AlmacenamientoDatos import guardar_parquet, leer_parquet


class Ejercicio2C:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self, df):
        print("Ejercicio 2.c")

        # Contamos las filas almacenadas antes del append
        filas_antes = leer_parquet(self.spark, RUTA_BRONZE_SENTIMIENTO).count()
        print(f"Filas antes del append: {filas_antes}")

        # Añadimos exactamente el mismo DataFrame en modo append
        guardar_parquet(df, RUTA_BRONZE_SENTIMIENTO, "append")

        # Volvemos a leer la carpeta y contamos las filas despues del append
        df_despues = leer_parquet(self.spark, RUTA_BRONZE_SENTIMIENTO)
        filas_despues = df_despues.count()

        print(f"Filas despues del append: {filas_despues}")
        print("Con append no se sustituyen los datos existentes, se añaden nuevos ficheros y al cargar otra vez los mismos datos las filas se duplican")

        return df_despues
