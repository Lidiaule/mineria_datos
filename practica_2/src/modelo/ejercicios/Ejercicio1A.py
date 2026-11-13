''' Ej1a: Crea una función que permita descargar el histórico de una acción concreta,
facilitando una fecha de inicio y una de fin, y lo almacene en un dataframe de
pyspark. Define para cada columna si permite nulos y por qué. '''

from src.modelo.funciones.DescargaYahoo import descargar_accion


class Ejercicio1A:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self, ticker, fecha_inicio, fecha_fin):
        print("Ejercicio 1.a")

        # Descargamos la accion
        df = descargar_accion(self.spark, ticker, fecha_inicio, fecha_fin)

        # Comprobamos el esquema y algunas lineas
        df.printSchema()
        df.show(5, truncate=False)

        # Decir si permite nulos y por que
        print("Date y Ticker no permiten nulos porque identifican la sesion y el activo")
        print("Open, High, Low, Close, Volume, Dividends y Stock Splits permiten nulos porque puede faltar informacion en alguna sesion")

        return df
