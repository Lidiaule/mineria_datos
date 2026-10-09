from pyspark.sql.functions import *
from pyspark.sql.types import *

class Ejercicio2:
    
    def apartado_a(self, df):
        print("Ejercicio 2.a")

        filas_iniciales = df.count()

        df = df.dropDuplicates()

        filas_finales = df.count()

        filas_eliminadas = filas_iniciales - filas_finales
        print(f"Se han eliminado {filas_eliminadas} filas")

        num_empresas = len(df.columns) - 1
        print(f"Número de empresas con información disponible: {num_empresas}")

        return df, filas_eliminadas, num_empresas


    def apartado_b(self, df):
        print("Ejercicio 2.b")

        fecha_inicio = (df.select(min("Fecha")).first()[0])

        fecha_fin = (df.select(max("Fecha")).first()[0])

        dias = df.count()
        
        print(f"Periodo temporal: desde {fecha_inicio} hasta {fecha_fin}")
        print(f"Días de información disponible: {dias}")

        print("El resultado es coherente ya que un año bursátil cuenta con aproximadamente 250 días laborables descontando fines de semana y festivos.")
        print("No es necesario buscar datos adicionales salvo que se requiera analizar días no lectivos sin cotización.")

        return fecha_inicio, fecha_fin, dias