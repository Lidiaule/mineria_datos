def anadir_sector_a_precios(df_ibex, df_empresas):
    """Añade a cada cotizacion el sector de la empresa mediante un inner join por Ticker"""
    return df_ibex.join(df_empresas.select("Ticker", "Sector"), on="Ticker", how="inner")


def integrar_precios_sentimiento(df_ibex, df_sentimiento, df_empresas):
    """Cruza precios, sector de empresa y sentimiento para construir la tabla de hechos"""
    
    # Primero incorporamos el sector a cada precio
    precios_sector = anadir_sector_a_precios(df_ibex, df_empresas)

    # Unificamos el nombre de la fecha para poder cruzar ambos DataFrames
    sentimiento = df_sentimiento.withColumnRenamed("Fecha", "Date" )

    # El hecho final conserva unicamente las combinaciones Fecha-Sector presentes en ambas fuentes
    return precios_sector.join(sentimiento, on=["Date", "Sector"], how="inner")


def construir_dimension_empresa(df_empresas):
    """Crea una dimension con una unica fila por ticker"""
    return (df_empresas.select("Ticker", "Empresa", "Sector", "Industria").dropDuplicates(["Ticker"]))


def construir_dimension_fecha(df_hechos):
    """Crea una dimension con una unica fila por fecha"""
    return (df_hechos.select("Date").dropDuplicates(["Date"]))


def anti_join(df_izquierda, df_derecha, columnas_clave):
    """Devuelve las filas de la izquierda que no encuentran pareja en la derecha"""
    return df_izquierda.join(df_derecha, on=columnas_clave, how="left_anti" )
