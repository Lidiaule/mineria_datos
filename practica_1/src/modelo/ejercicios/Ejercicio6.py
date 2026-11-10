'''Ej6: VersionAsOf lee la versión antigua (demuestra que el dato sigue recuperable),
pero no cambia la tabla actual. Deja la tabla realmente como estaba en el EJ4,
usando RESTORE.'''

from src.modelo.configuracion.Configuracion import RUTA_BRONZE_IBEX
from src.modelo.funciones.AlmacenamientoDatos import leer_delta
from src.modelo.funciones.OperacionesDelta import (leer_version, restaurar_version, obtener_version_actual)

class Ejercicio6:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self, version_ejercicio4):
        print("Ejercicio 6")

        # Guardamos la version actual
        version_antes = obtener_version_actual(self.spark, RUTA_BRONZE_IBEX)

        # Usamos versionAsOf para leer una version anterior 
        df_antiguo = leer_version(self.spark, RUTA_BRONZE_IBEX, version_ejercicio4)
        print(f"Filas leidas con versionAsOf: {df_antiguo.count()}")

        version_despues_lectura = obtener_version_actual(self.spark, RUTA_BRONZE_IBEX)

        print(f"Version actual antes de versionAsOf: {version_antes}")
        print(f"Version actual despues de versionAsOf: {version_despues_lectura}")

        # Usamos RESTORE para dejar la tabla como estaba en el EJ4
        restaurar_version(self.spark, RUTA_BRONZE_IBEX, version_ejercicio4)

        nueva_version = obtener_version_actual(self.spark, RUTA_BRONZE_IBEX)

        print(f"Tabla restaurada al estado del Ej4 (version {version_ejercicio4}).")
        print(f"Nueva version creada por RESTORE: {nueva_version}")
        print("Filas despues del RESTORE: "f"{leer_delta(self.spark, RUTA_BRONZE_IBEX).count()}")
