from pathlib import Path
from pyspark.sql import SparkSession


class SparkSessionPractica:

    @staticmethod
    def crear_sesion(path_jar="./lib/mysql-connector-j-9.7.0.jar"):
        ruta_jar = str(Path(path_jar).resolve())

        spark = (
            SparkSession.builder
            .master("local[*]")
            .appName("IBEX35")
            .config("spark.driver.extraClassPath", ruta_jar)
            .getOrCreate()
        )

        return spark