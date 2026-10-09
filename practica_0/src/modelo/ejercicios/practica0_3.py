from pyspark.sql.functions import *


class Ejercicio3:

    def apartado_a(self, df):
        print("Ejercicio 3.a")

        df = df.withColumnRenamed("Fecha", "Día")
        df.show(10)

        empresas = [c for c in df.columns if c != "Día"]

        resultados = []

        for emp in empresas:
            print(f"Estadisticas: {emp}")
            estadisticas = df.select(
                avg(col(emp)).alias("Media anual"),
                max(col(emp)).alias("Max anual"),
                min(col(emp)).alias("Min anual"))
            estadisticas.show()
            resultados.append((emp, estadisticas))

        return df, resultados

    def deficiency_notice(self, df):

        df = df.withColumn("Deficiency Notice UNI", when(col("UNI") < 1.0, True).otherwise(False))
        df.show(100)
        return df

    def apartado_b(self):
        print("Ejercicio 3.b")

        print("Son las empresas del índice IBEX-35 en 2024; los NULL de PUIG se deben a su salida a bolsa el 3/5/2024 (Fuente: BME).")

        print("Los NULL no afectan a funciones de agregación como avg() o min() porque Spark los ignora automáticamente en el cálculo.")

