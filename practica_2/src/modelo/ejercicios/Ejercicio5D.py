'''Ej5d: Muestra el history() (verás las versiones de los Ej5b y Ej5c) y lee con
versionAsOf a la versión de antes del Ej5a. Comprueba si todo esta igual.'''


# Se ha utilizado IA para comprender ciertas funciones(history() y versionAsOf)
from pyspark.sql.functions import col
from src.modelo.configuracion.Configuracion import RUTA_BRONZE_IBEX
from src.modelo.funciones.OperacionesDelta import mostrar_historial, leer_version


class Ejercicio5D:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self, version_antes_5a, version_ejercicio4):
        print("Ejercicio 5.d")

        # Mostramos el history()
        mostrar_historial(self.spark, RUTA_BRONZE_IBEX)

        # Leemos la version anterior al Ej5a
        df_antiguo = leer_version(self.spark, RUTA_BRONZE_IBEX, version_antes_5a)

        print(f"Version anterior al Ej5a: {version_antes_5a}")
        print(f"Version guardada al terminar el Ej4: {version_ejercicio4}")

        # Comprobamos el esquema (BBVA vuelve a estar presente en esa version)
        df_antiguo.printSchema()
        print(f"Numero de filas recuperadas: {df_antiguo.count()}")
        print("Filas de BBVA recuperadas: " f"{df_antiguo.filter(col('Ticker') == 'BBVA.MC').count()}")
        print("La version recuperada coincide con el estado del Ej4: vuelve a aparecer BBVA y la columna Close_mas5 todavia no existe")