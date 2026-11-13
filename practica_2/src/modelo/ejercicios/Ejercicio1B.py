'''Ej1b: Usando la función anterior, descarga los últimos 2 años (último día 1 de
octubre de 2026) de todas las empresas del IBEX-35 y guárdalo crudo en la capa
bronce (lo veremos más adelante que significa), en formato Parquet:'''


from src.modelo.configuracion.Configuracion import RUTA_BRONZE_IBEX
from src.modelo.funciones.DescargaYahoo import descargar_ibex
from src.modelo.funciones.AlmacenamientoDatos import guardar_parquet
from src.modelo.funciones.LimpiezaDatos import limpiar_nombres_columnas_delta


class Ejercicio1B:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 1.b")

        # Descargamos dos años de historico de todas las empresas
        df_ibex = descargar_ibex(self.spark, "2024-10-01", "2026-10-02")

        # Limpiamos los datos
        df_ibex = limpiar_nombres_columnas_delta(df_ibex)        
        
        # Guardamos el dato crudo en la capa bronze en formato Parquet
        guardar_parquet(df_ibex, RUTA_BRONZE_IBEX, "overwrite")

        return df_ibex
