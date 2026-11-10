from delta.tables import DeltaTable


def convertir_parquet_a_delta(spark, ruta):
    """Convierte una carpeta Parquet existente a Delta sin reescribir los datos"""
    DeltaTable.convertToDelta(spark, f"parquet.`{ruta}`")


def obtener_tabla_delta(spark, ruta):
    """Obtiene el objeto DeltaTable asociado a una ruta"""
    return DeltaTable.forPath(spark, ruta)


def mostrar_historial(spark, ruta):
    """Muestra el historial completo de versiones de una tabla Delta"""
    obtener_tabla_delta(spark, ruta).history().show(truncate=False)


def obtener_version_actual(spark, ruta):
    """Devuelve como entero el numero de la version actual de una tabla Delta"""
    return (obtener_tabla_delta(spark, ruta).history(1).select("version").collect()[0][0])


def hacer_merge_insert_all(spark, ruta_destino, nuevos, condicion):
    """Inserta mediante MERGE las filas que todavia no existen en la tabla destino.
    whenNotMatchedInsertAll() permite que una segunda ejecucion no duplique las claves existentes."""
    destino = obtener_tabla_delta(spark, ruta_destino)

    (destino.alias("d").merge(nuevos.alias("n"), condicion).whenNotMatchedInsertAll().execute())


def eliminar_filas(spark, ruta, condicion):
    """Elimina de una tabla Delta las filas que cumplen una condicion"""
    obtener_tabla_delta(spark, ruta).delete(condicion)


def leer_version(spark, ruta, version):
    """Lee una version historica sin modificar el estado actual de la tabla"""
    return (spark.read.format("delta").option("versionAsOf", version).load(ruta))


def restaurar_version(spark, ruta, version):
    """Restaura realmente una tabla al contenido de una version anterior"""
    obtener_tabla_delta(spark, ruta).restoreToVersion(version)
