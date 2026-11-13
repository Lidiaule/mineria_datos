'''Ej3: Convierte las carpetas de bronze (ibex y sentimiento), que ahora son Parquet,
en tablas Delta, sin reescribir los datos. Muestra el historial y comenta qué ha
aparecido en la carpeta (_delta_log).'''

from src.modelo.configuracion.Configuracion import (RUTA_BRONZE_IBEX, RUTA_BRONZE_SENTIMIENTO)
from src.modelo.funciones.OperacionesDelta import (convertir_parquet_a_delta, mostrar_historial)


class Ejercicio3:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 3")

        # Convertimos ambas carpetas Parquet a Delta sin reescribir los datos
        convertir_parquet_a_delta(self.spark, RUTA_BRONZE_IBEX)
        
        convertir_parquet_a_delta(self.spark, RUTA_BRONZE_SENTIMIENTO)

        # Comprobamos el historial generado por Delta
        print("Historial IBEX:")
        mostrar_historial(self.spark, RUTA_BRONZE_IBEX)

        print("Historial sentimiento:")
        mostrar_historial(self.spark, RUTA_BRONZE_SENTIMIENTO)

        print("Ha aparecido la carpeta _delta_log, que guarda el registro de transacciones y permite mantener el historial de la tabla Delta.")
