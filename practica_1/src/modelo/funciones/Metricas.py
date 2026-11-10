from pyspark.sql.functions import col, lag, when
from pyspark.sql.window import Window


def anadir_variacion_diaria(df):
    """Añade la variacion porcentual del cierre respecto a la fila anterior de la misma empresa.
    Se usa Window.orderBy(), lag(), when(), col() y withColumn(), funciones vistas en clase"""

    # Ordenamos por ticker y por fecha para que las sesiones de cada empresa queden juntas
    ventana = Window.orderBy("Ticker", "Date")

    # Recuperamos el ticker y el cierre de la fila anterior
    ticker_anterior = lag("Ticker").over(ventana)
    close_anterior = lag("Close").over(ventana)

    # Formula de variacion porcentual respecto al cierre anterior
    variacion = ((col("Close") - close_anterior)/ close_anterior) * 100

    # Solo calculamos la variacin cuando la fila anterior pertenece al mismo ticker
    # Asi evitamos comparar la ultima sesion de una empresa con la primera de la siguiente
    df = df.withColumn("VariacionDiaria", when(col("Ticker") == ticker_anterior, variacion))

    return df


def anadir_rango_diario(df):
    """Añade la diferencia entre el maximo y el minimo de cada sesion bursatil"""

    return df.withColumn("RangoDiario", col("High") - col("Low"))
