def leer_csv(spark, ruta, separador=";", cabecera=True):
    """Lee un CSV y devuelve un DataFrame de Spark"""
    return (spark.read.option("header", cabecera).option("sep", separador).csv(ruta))


def guardar_parquet(df, ruta, modo="overwrite"):
    """Guarda un DataFrame en formato Parquet"""
    df.write.mode(modo).parquet(ruta)


def leer_parquet(spark, ruta):
    """Lee una carpeta o fichero Parquet"""
    return spark.read.parquet(ruta)


def guardar_delta(df, ruta, modo="overwrite", merge_schema=False):
    """Guarda un DataFrame como tabla Delta,
    merge_schema=True activa la evolucion de esquema cuando el cambio es intencionado"""
    escritor = df.write.format("delta").mode(modo)

    if merge_schema:
        escritor = escritor.option("mergeSchema", "true")

    escritor.save(ruta)


def leer_delta(spark, ruta):
    """Lee una tabla Delta desde su ruta"""
    return spark.read.format("delta").load(ruta)


def exportar_parquet(df, ruta, modo="overwrite", particion=None):
    """Exporta un DataFrame a Parquet, con particionado opcional"""
    escritor = df.write.mode(modo)

    if particion:
        escritor = escritor.partitionBy(particion)

    escritor.parquet(ruta)
    

