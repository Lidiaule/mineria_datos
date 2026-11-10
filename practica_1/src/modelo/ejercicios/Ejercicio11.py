'''Ej11 (opcional): Con un anti-join, muestra (a) los precios que se quedan sin
sentimiento y (b) el sentimiento sin precios. Comenta que sucede y como lo
solucionas.'''

from src.modelo.configuracion.Configuracion import (RUTA_SILVER_IBEX, RUTA_SILVER_SENTIMIENTO, RUTA_SILVER_EMPRESAS)
from src.modelo.funciones.AlmacenamientoDatos import leer_delta
from src.modelo.funciones.IntegracionDatos import anadir_sector_a_precios, anti_join


class Ejercicio11:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 11")

        # Leemos las fuentes silver necesarias para comprobar que registros no cruzan
        df_ibex = leer_delta(self.spark, RUTA_SILVER_IBEX)
        df_empresas = leer_delta(self.spark, RUTA_SILVER_EMPRESAS)
        df_sentimiento = leer_delta(self.spark, RUTA_SILVER_SENTIMIENTO).withColumnRenamed("Fecha", "Date")

        # Añadimos el sector a las cotizaciones
        df_precios = anadir_sector_a_precios(df_ibex, df_empresas)

        # Generamos las claves unicas necesarias para comparar
        claves_sentimiento = (df_sentimiento.select("Date", "Sector").dropDuplicates(["Date", "Sector"]))
        claves_precios = (df_precios.select("Date", "Sector").dropDuplicates(["Date", "Sector"]))

        # Anti-join en ambos sentidos.
        precios_sin_sentimiento = anti_join(df_precios, claves_sentimiento, ["Date", "Sector"])
        sentimiento_sin_precios = anti_join(df_sentimiento, claves_precios, ["Date", "Sector"])

        print("Precios que se quedan sin sentimiento:")
        precios_sin_sentimiento.show(truncate=False)

        print("Sentimiento que se queda sin precios:")
        sentimiento_sin_precios.show(truncate=False)

        print("Hay filas sin pareja porque ambas fuentes no siempre coinciden en fecha y sector. "
            "El inner join conserva solo las coincidencias de ambas")

        return precios_sin_sentimiento, sentimiento_sin_precios
