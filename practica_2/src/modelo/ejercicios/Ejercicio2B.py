'''Ej2b: Guarda el sentimiento crudo en la capa bronze en formato Parquet, en su
propia carpeta (data/lake/bronze/sentimiento). Muestra cuántas filas se han
escrito.'''

from src.modelo.configuracion.Configuracion import RUTA_BRONZE_SENTIMIENTO
from src.modelo.funciones.AlmacenamientoDatos import guardar_parquet


class Ejercicio2B:
    def ejecutar(self, df):
        print("Ejercicio 2.b")

        # Guardamos el sentimiento crudo en la capa bronze
        guardar_parquet(df, RUTA_BRONZE_SENTIMIENTO, "overwrite")

        # Filas escritas
        print(f"Se han escrito {df.count()} filas.")

        return df
