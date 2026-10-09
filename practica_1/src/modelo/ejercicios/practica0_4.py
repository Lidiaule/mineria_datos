from pyspark.sql.functions import *


class Ejercicio4:

    def ejecutar(self, df):
        
        print("Ejercicio 4")
        
        empresas = [c for c in df.columns if c not in ["Día", "Deficiency Notice UNI"]]

        expresiones = []

        for emp in empresas:

            variacion = ((last(col(emp)) - first(col(emp))) / first(col(emp))) * 100

            clasificacion = (
                when(variacion >= 15, "Subida Fuerte")
                .when(variacion > 1, "Subida")
                .when(variacion >= -1, "Neutra")
                .when(variacion > -15, "Bajada")
                .otherwise("Bajada Fuerte"))
            
            expresiones.append(clasificacion.alias(emp))

        resultado = df.select(expresiones)
        resultado.show(truncate=False)
        
        return resultado