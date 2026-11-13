'''Ej10: Integra todas las fuentes en la capa y guárdala en data/lake/gold. '''


# Se utilizo la IA en este ejercicio para plantear la integracion de precios y comprender el modelo estrella de la capa gold
from src.modelo.configuracion.Configuracion import (RUTA_SILVER_IBEX, RUTA_SILVER_SENTIMIENTO, RUTA_SILVER_EMPRESAS, RUTA_GOLD_HECHOS, RUTA_GOLD_DIM_EMPRESA, RUTA_GOLD_DIM_FECHA)
from src.modelo.funciones.AlmacenamientoDatos import leer_delta, guardar_delta
from src.modelo.funciones.IntegracionDatos import (integrar_precios_sentimiento, construir_dimension_empresa, construir_dimension_fecha)


class Ejercicio10:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 10")

        # Leemos las tres fuentes ya limpias de la capa silver
        df_ibex = leer_delta(self.spark, RUTA_SILVER_IBEX)
        df_sentimiento = leer_delta(self.spark, RUTA_SILVER_SENTIMIENTO)
        df_empresas = leer_delta(self.spark, RUTA_SILVER_EMPRESAS)

        # Construimos el hecho integrado y las dimensiones del modelo en estrella
        df_hechos = integrar_precios_sentimiento(df_ibex, df_sentimiento, df_empresas)
        df_dim_empresa = construir_dimension_empresa(df_empresas)
        df_dim_fecha = construir_dimension_fecha(df_hechos)

        # Guardamos cada tabla gold como una tabla Delta independiente
        guardar_delta(df_hechos, RUTA_GOLD_HECHOS, "overwrite")
        guardar_delta(df_dim_empresa, RUTA_GOLD_DIM_EMPRESA, "overwrite")
        guardar_delta(df_dim_fecha, RUTA_GOLD_DIM_FECHA, "overwrite")

        return df_hechos, df_dim_empresa, df_dim_fecha
