'''Ej12 (opcional): Vuelve al estudio realizado en el Ej7 y piensa que datos te gustaría
ver en el dashboard (adicionales a los datos tal cual) que se hará en power BI (por
ejemplo, la variación de precio respecto al día anterior). Realiza al menos dos
operaciones/cálculos y guárdalos en una nueva columna.'''


# Utilicé IA para entender lag() y las ventanas de Spark
from src.modelo.configuracion.Configuracion import (RUTA_GOLD_HECHOS, RUTA_GOLD_HECHOS_METRICAS)
from src.modelo.funciones.AlmacenamientoDatos import leer_delta, guardar_delta
from src.modelo.funciones.Metricas import anadir_variacion_diaria, anadir_rango_diario


class Ejercicio12:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 12")

        # Utilizamos la tabla de hechos de la capa gold
        df = leer_delta(self.spark, RUTA_GOLD_HECHOS)

        # Añadimos dos metricas utiles para el futuro dashboard de Power BI
        df = anadir_variacion_diaria(df)
        df = anadir_rango_diario(df)

        # Guardamos una tabla gold adicional con las nuevas columnas calculadas
        guardar_delta(df, RUTA_GOLD_HECHOS_METRICAS, "overwrite")
        print("Resultado de las métricas añadidas:")

        df.select("Ticker", "Date", "Close", "VariacionDiaria", "RangoDiario").show(5)

        return df
