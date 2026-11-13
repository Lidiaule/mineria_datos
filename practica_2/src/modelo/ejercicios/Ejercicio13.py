'''Ej13: Exporta la gold a Parquet en data/export/gold, lista para Power BI. (Tienes que
elegir como lo vas a guardar). Investiga más sobre la forma de estrella para
guardar los datos (Cuanto más eficiente lo hagas, mejor funcionará la siguiente
práctica. Pregunta a tu profesor si tienes dudas una vez tengas el modelo).
Justifícalo en UN párrafo en el pdf.'''


# He usado IA para poder tener en cuenta el uso posterior de Power BI, y para la detección y correccion de errores surgidos durante la ejecucion
from src.modelo.configuracion.Configuracion import (RUTA_GOLD_HECHOS_METRICAS, RUTA_GOLD_DIM_EMPRESA, RUTA_GOLD_DIM_FECHA, RUTA_EXPORT_GOLD)
from src.modelo.funciones.AlmacenamientoDatos import (leer_delta)


class Ejercicio13:

    def __init__(self, spark):
        self.spark = spark

    def ejecutar(self):

        print("Ejercicio 13")

        # Leemos la tabla de hechos Gold con las meétricas del ejercicio 12
        hechos = leer_delta(self.spark, RUTA_GOLD_HECHOS_METRICAS)

        # Leemos las dimensiones creadas en el ejercicio 10
        dim_empresa = leer_delta(self.spark, RUTA_GOLD_DIM_EMPRESA)

        dim_fecha = leer_delta(self.spark, RUTA_GOLD_DIM_FECHA)        
        
        # Exportamos cada tabla a Parquet en una sola partición para que Power BI tenga un unico fichero por tabla
        hechos.coalesce(1).write.mode("overwrite").parquet(RUTA_EXPORT_GOLD + "/hechos")

        dim_empresa.coalesce(1).write.mode("overwrite").parquet(RUTA_EXPORT_GOLD + "/dim_empresa")

        dim_fecha.coalesce(1).write.mode("overwrite").parquet(RUTA_EXPORT_GOLD + "/dim_fecha")

        print("Exportacion Gold realizada correctamente.")
