from pyspark.sql.functions import *


class Ejercicio5:

    def ejecutar(self, df):
        print("Ejercicio 5")

        empresas = [c for c in df.columns if c not in ["Día", "Deficiency Notice UNI"]]

        for emp in empresas:
            cuartiles = df.approxQuantile(emp, [0.25, 0.50, 0.75], 0.01)

            q1 = cuartiles[0]
            q2 = cuartiles[1]
            q3 = cuartiles[2]

            col_cuartil = (f"{emp}Cuartil")

            df = df.withColumn(col_cuartil, when(col(emp) <= q1, "q1")
                .when(col(emp) <= q2, "q2")
                .when(col(emp) <= q3, "q3")
                .otherwise("q4"))
            
        df.show(1, truncate=False)
        return df


    def obtener_aena_bbva(self, df):

        columnas = ["Día", "AENA", "AENACuartil", "BBVA", "BBVACuartil"]

        columnas_validas = [c for c in columnas if c in df.columns]

        resultado = df.select(columnas_validas)
        resultado.show(resultado.count(), truncate=False)
        
        return resultado