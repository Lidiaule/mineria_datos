'''Ej9: Deja los datos de la api de yahoo finance limpos (si es necesario) y guárdalos
en data/lake/silver/ibex. Si necesitas más datos (Ej7) guarda en una dimensión (o
varias) aparte tanto en bronce (datos en crudo) como en silver (datos corregidos)
la información. Muestra la/s fila/s 5.'''

from src.modelo.configuracion.Configuracion import (RUTA_BRONZE_IBEX, RUTA_SILVER_IBEX, RUTA_BRONZE_EMPRESAS, RUTA_SILVER_EMPRESAS)
from src.modelo.funciones.AlmacenamientoDatos import leer_delta, guardar_delta
from src.modelo.funciones.LimpiezaDatos import limpiar_ibex, limpiar_empresas


class Ejercicio9:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 9")

        # Dejamos los datos limpios y los guardamos en la silver
        df_ibex = limpiar_ibex(leer_delta(self.spark, RUTA_BRONZE_IBEX))
        guardar_delta(df_ibex, RUTA_SILVER_IBEX, "overwrite")

        # Limpiamos la dimension empresa y la almacenamos en silver
        df_empresas = limpiar_empresas(leer_delta(self.spark, RUTA_BRONZE_EMPRESAS))
        guardar_delta(df_empresas, RUTA_SILVER_EMPRESAS, "overwrite")

        # Mostramos fila 5
        print("Fila 5 de silver/ibex:")
        print(df_ibex.head(5)[4])

        print("Fila 5 de silver/empresas:")
        print(df_empresas.head(5)[4])

        return df_ibex, df_empresas
