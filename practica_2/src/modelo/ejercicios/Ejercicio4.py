'''Ej4: Visualiza la versión actual de la base de datos. Ahora vamos a incluir datos
nuevos. Vuelve a descargar los precios del IBEX-35 pero hasta hoy. Haz MERGE
sobre la clave (Ticker, Fecha):
o En la primera ejecución, comprueba que se insertan los días nuevos (el
número de filas sube).
o Ejecútalo una segunda vez y comprueba que pasa.'''

# He usado IA en este ejercicio para dudas que me han surgido durante la implementacion del codigo con ciertas funciones (MERGE) en Delta Lake
# y para problemas surgidos durante la ejecucion del programa
from src.modelo.configuracion.Configuracion import RUTA_BRONZE_IBEX
from src.modelo.funciones.AlmacenamientoDatos import leer_delta
from src.modelo.funciones.DescargaYahoo import descargar_ibex
from src.modelo.funciones.OperacionesDelta import (hacer_merge_insert_all, obtener_version_actual)
from src.modelo.funciones.LimpiezaDatos import limpiar_nombres_columnas_delta

class Ejercicio4:
    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):
        print("Ejercicio 4")

        # Version actual de BD
        version_actual = obtener_version_actual(self.spark, RUTA_BRONZE_IBEX)
        print(f"Version actual: {version_actual}")

        # Descargamos los precios desde el inicio hasta hoy
        nuevos = descargar_ibex(self.spark, "2024-10-01")
        
        nuevos = limpiar_nombres_columnas_delta(nuevos)
        
        # Para saber si una cotizacion ya existe en la tabla Delta
        condicion = "d.Ticker = n.Ticker AND d.Date = n.Date"

        # Contamos las filas antes del primer MERGE
        filas_antes = leer_delta(self.spark, RUTA_BRONZE_IBEX).count()

        # Primer MERGE: insertamos dias nuevos
        hacer_merge_insert_all(self.spark, RUTA_BRONZE_IBEX, nuevos, condicion)

        filas_primera = leer_delta(self.spark, RUTA_BRONZE_IBEX).count()

        print(f"Filas antes del primer MERGE: {filas_antes}")
        print(f"Filas despues del primer MERGE: {filas_primera}")

        # Segundo MERGE 
        hacer_merge_insert_all(self.spark, RUTA_BRONZE_IBEX, nuevos, condicion)

        filas_segunda = leer_delta(self.spark, RUTA_BRONZE_IBEX).count()

        print(f"Filas despueés del segundo MERGE: {filas_segunda}")
        print("La segunda ejecucion no duplica datos porque MERGE solo inserta las claves Ticker-Date que todavia no existen")

        # Guardamos la version 
        return obtener_version_actual(self.spark, RUTA_BRONZE_IBEX)
