'''Ej7: Analiza los datos e incluye una reflexión de como podrías tener en cuenta la
información del experto en los datos que puedes obtener de yahoo finance.
(Investiga que datos tiene la API de yahoo u otras interesantes). Justifícalo en el
pdf'''

from src.modelo.configuracion.Configuracion import RUTA_BRONZE_EMPRESAS
from src.modelo.funciones.DescargaYahoo import descargar_informacion_empresas
from src.modelo.funciones.AlmacenamientoDatos import guardar_delta


class Ejercicio7:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 7")

        # Descargamos datos descriptivos para poder relacionar cada ticker con su sector.
        df_empresas = descargar_informacion_empresas(self.spark)

        # Guardamos esta fuente adicional en bronze antes de limpiarla en el Ej9.
        guardar_delta(df_empresas, RUTA_BRONZE_EMPRESAS, "overwrite")

        return df_empresas
