import sys
import os

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

class SparkSessionPractica:
    # Creamos una única SparkSession configurada para trabajar con Delta Lake

    @staticmethod
    def crear_sesion():
        # Constructor de la sesion Spark
        builder = (SparkSession.builder
            .appName("IBEX35")
            .master("local[*]")
            # Ruta relativa al conector JDBC
            .config("spark.driver.extraClassPath", "./lib/mysql-connector-j-9.7.0.jar")
            # Activamos las extensiones necesarias de Delta Lake
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            # Hacemos que el catalogo de Spark utilice Delta
            .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog"))

        # Añade automaticamente los jars de Delta instalados con pip y crea la sesion
        spark = configure_spark_with_delta_pip(builder).getOrCreate()
        spark.sparkContext.setLogLevel("ERROR")
        return spark
