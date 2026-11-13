'''Ej2a: Guarda el fichero sentimiento_ibex.csv en un DataFrame de PySpark. No abrir
el csv. Observa y comenta que todas las columnas llegan como texto (un CSV no
guarda los tipos). '''

from src.modelo.configuracion.Configuracion import RUTA_CSV_SENTIMIENTO
from src.modelo.funciones.AlmacenamientoDatos import leer_csv


class Ejercicio2A:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 2.a")

        # Guardamos sentimiento en un DataFrame de PySpark
        df = leer_csv(self.spark, RUTA_CSV_SENTIMIENTO, separador=";", cabecera=True)

        df.printSchema()
        print("Todas las columnas llegan como StringType porque un CSV no guarda los tipos de datos, por eso depues necesitaremos convertir las columnas al tipo adecuado")

        return df
