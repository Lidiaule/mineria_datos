from pyspark.sql.functions import *
from pyspark.sql.window import Window


class Ejercicio6: # Se utilizó IA, concretamente Gemini

    def ejecutar(self, df):
        print("Ejercicio 6")

        col_fecha = "Dia" if "Dia" in df.columns else "Día"
        windowSpec = Window.orderBy(col_fecha)

        columnas_no_empresa = ["Dia", "Día", "Deficiency Notice UNI"]
        empresas = [c for c in df.columns if c not in columnas_no_empresa and not c.endswith("Cuartil")]

        for emp in empresas:
            val_anterior = lag(col(emp)).over(windowSpec)

            variacion_diaria = ((col(emp) - val_anterior) / val_anterior) * 100
            
            col_cambio = f"{emp}CambioSignificativo"

            df = df.withColumn(
                col_cambio,
                when(
                    val_anterior.isNotNull() & (abs(variacion_diaria) > 8),
                    concat(round(variacion_diaria, 2).cast("string"), lit("%"))
                ).otherwise("-")
            )

        print("Fila 15 del DataFrame")
        fila_15 = df.orderBy(col_fecha).collect()[14]
        print(fila_15)

        print("\n Interpretación e Investigación de Variaciones Significativas:")
        print("Las fluctuaciones extremas superiores al 8% diarios corresponden a eventos extraordinarios de alta volatilidad:")
        print("1. Grifols: Grandes caidas que respondieron a la publicacion del informe del fondo bajista Gotham City Research, la presentación de resultados no auditados y rebajas de calificación por Moody's, etc.")
        print("2. Naturgy: Fuerte retroceso tras la ruptura oficial de las negociaciones entre CriteriaCaixa y el grupo emiratí Taqa para el lanzamiento de una Oferta Pública de Adquisición (OPA) de acciones.")
        print("3. Puig Brands: Tras su salida en bolsa tuvo un gran descenso, del cual recupero parte tras reporta aceleracion en ventas del tercer trimestre")
        print("4. Laboratorios Farmaceuticos Rovi: Tuvo una caida devido a un anuncio de cancelción del proceso de venta de su división de fabricación para terceros (CDMO) y la consiguiente revisión a la baja de sus guías de negocio.")
        print("\nReferencias de consulta:")
        print("- Comunicados de Hechos Relevantes ante la CNMV; Informes de Gotham City Research; Informes de Auditoría de KPMG (2024).")
        print("- Comunicado oficial de CriteriaCaixa a la CNMV (10/06/2024); Registro Público CNMV.")
        print("- Informe de Resultados 1S/3T 2024 de Puig Brands S.A.; Registro CNMV.")
        print("- Información Privilegiada CNMV — Laboratorios Farmacéuticos Rovi S.A.")

        return df