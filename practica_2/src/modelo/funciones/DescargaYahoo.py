import yfinance as yf
from pyspark.sql.types import (StructType, StructField, DateType, DoubleType, LongType, StringType)
from src.modelo.configuracion.Configuracion import TICKERS_IBEX


def descargar_accion(spark, ticker, fecha_inicio, fecha_fin=None):
    """Descarga el historico de una accion con yfinance y lo convierte
    en un DataFrame de Spark. Se define explicitamente el esquema para indicar los tipos de datos
    y qué columnas permiten valores nulos"""

    # Si no se facilita fecha_fin, Yahoo devuelve los datos desde fecha_inicio hasta la fecha disponible mas reciente
    if fecha_fin is None:
        pdf = yf.Ticker(ticker).history(start=fecha_inicio, interval="1d", auto_adjust=False)
    else:
        pdf = yf.Ticker(ticker).history(start=fecha_inicio, end=fecha_fin, interval="1d",auto_adjust=False)

    # yfinance guarda Date como indice, reset_index() lo convierte en una columna para que Spark pueda conservarla
    pdf.reset_index(inplace=True)

    # Añadimos el ticker para identificar a que empresa pertenece cada cotizacion
    pdf["Ticker"] = ticker

    # Convertimos Date a fecha sin hora para que Spark pueda almacenarla como DateType
    pdf["Date"] = pdf["Date"].dt.date

    # Definimos explicitamente el esquema.
    # Date y Ticker no permiten nulos porque identifican la sesion bursatil y la empresa
    # El resto de columnas si permiten nulos porque Yahoo puede no disponer de algun dato concreto
    esquema = StructType([
        StructField("Date", DateType(), False),
        StructField("Open", DoubleType(), True),
        StructField("High", DoubleType(), True),
        StructField("Low", DoubleType(), True),
        StructField("Close", DoubleType(), True),
        StructField("Adj Close", DoubleType(), True),
        StructField("Volume", LongType(), True),
        StructField("Dividends", DoubleType(), True),
        StructField("Stock Splits", DoubleType(), True),
        StructField("Ticker", StringType(), False)])

    # Creamos el DataFrame de Spark utilizando el esquema definido
    df = spark.createDataFrame(pdf, schema=esquema)

    return df


def descargar_ibex(spark, fecha_inicio, fecha_fin=None):
    """Descarga todos los tickers definidos en Configuracion.py y apila sus filas utilizando union()"""
    dataframes = []

    # Reutilizamos descargar_accion() para no repetir la logica de descarga de Yahoo Finance
    for ticker in TICKERS_IBEX:
        df_ticker = descargar_accion(spark, ticker, fecha_inicio, fecha_fin)

        dataframes.append(df_ticker)

    # Empezamos por el primer DataFrame
    df_total = dataframes[0]

    # Apilamos debajo los DataFrames del resto de empresas
    for df_ticker in dataframes[1:]:
        df_total = df_total.union(df_ticker)

    return df_total


def descargar_informacion_empresas(spark):
    """Obtiene informacion descriptiva de cada empresa para construir
    la dimension empresa.Esta informacion permite relacionar posteriormente cada ticker
    con su nombre, sector e industria"""
    filas = []

    for ticker in TICKERS_IBEX:
        info = yf.Ticker(ticker).info

        filas.append((ticker, info.get("longName"), info.get("sector"), info.get("industry")))

    # Creamos el DataFrame de Spark indicando los nombres de las columnas
    df = spark.createDataFrame(filas, ["Ticker", "Empresa", "Sector", "Industria"])

    return df