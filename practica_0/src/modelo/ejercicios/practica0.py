from pyspark.sql.functions import *
from pyspark.sql.types import *

# Ejercicio 1
class Ejercicio1:

    def __init__(self, spark, path_csv):
        self.spark = spark
        self.path_csv = path_csv

    def apartado_a(self):
        print("Ejercicio 1.a")

        df = (self.spark.read.option("header", True).option("sep", ";").option("dateFormat", "dd/MM/yyyy").csv(self.path_csv))
        
        df.printSchema()

        df = df.withColumn("Fecha", to_date(col("Fecha"), "dd/MM/yyyy"))

        for col_name in df.columns:
            if col_name != "Fecha":
                df = df.withColumn(col_name, col(f"`{col_name}`").cast("double"))

        df.printSchema()
        df.show(6)
        
        return df


    def apartado_b(self, df):
        print("Ejercicio 1.b")

        for col_name in df.columns:
            if ".MC" in col_name:
                new_name = col_name.replace(".MC", "")
                df = df.withColumnRenamed(col_name, new_name)
                
        df.show(6)

        return df


    def apartado_c(self): # Se utilizó IA, concretamente Gemini
        print("Ejercicio 1.c")

        schema_ibex = StructType([

            StructField("Fecha", DateType(), True),

            StructField("Iberdrola", DoubleType(), True),
            StructField("Repsol", DoubleType(), True),
            StructField("Naturgy", DoubleType(), True),
            StructField("Endesa", DoubleType(), True),
            StructField("Enagas", DoubleType(), True),
            StructField("Redeia", DoubleType(), True),

            StructField("Banco Santander", DoubleType(), True),
            StructField("BBVA", DoubleType(), True),
            StructField("CaixaBank", DoubleType(), True),
            StructField("Bankinter", DoubleType(), True),
            StructField("Banco Sabadell", DoubleType(), True),
            StructField("Unicaja Banco", DoubleType(), True),

            StructField("Mapfre", DoubleType(), True),
            StructField("ACS", DoubleType(), True),
            StructField("Acciona", DoubleType(), True),
            StructField("Acciona Energia", DoubleType(), True),
            StructField("Acerinox", DoubleType(), True),
            StructField("ArcelorMittal", DoubleType(), True),
            StructField("Sacyr", DoubleType(), True),
            StructField("Cellnex", DoubleType(), True),
            StructField("Telefonica", DoubleType(), True),
            StructField("Aena", DoubleType(), True),
            StructField("Ferrovial", DoubleType(), True),
            StructField("Inditex", DoubleType(), True),
            StructField("Amadeus", DoubleType(), True),
            StructField("IAG", DoubleType(), True),
            StructField("Grifols", DoubleType(), True),
            StructField("Fluidra", DoubleType(), True),
            StructField("Solaria", DoubleType(), True),
            StructField("Laboratorios Rovi", DoubleType(), True),
            StructField("Logista", DoubleType(), True),
            StructField("Indra", DoubleType(), True),
            StructField("Melia Hotels", DoubleType(), True),
            StructField("Puig Brands", DoubleType(), True),
            StructField("Inmobiliaria Colonial", DoubleType(), True),
            StructField("Merlin Properties", DoubleType(), True)
        ])

        df = (self.spark.read.option("header", True).option("sep", ";").option("dateFormat", "dd/MM/yyyy").schema(schema_ibex)
            .csv(self.path_csv))

        df.printSchema()
        df.show(6)

        return df