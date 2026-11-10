# Archivo central de configuracion: contiene todas las rutas

# Fuente CSV de sentimiento
RUTA_CSV_SENTIMIENTO = "data/sentimiento_ibex.csv"

# Capa bronze: datos crudos o practicamente sin transformar
RUTA_BRONZE_IBEX = "data/lake/bronze/ibex"
RUTA_BRONZE_SENTIMIENTO = "data/lake/bronze/sentimiento"
RUTA_BRONZE_EMPRESAS = "data/lake/bronze/empresas"

# Capa silver: datos limpios, tipados y sin duplicados
RUTA_SILVER_IBEX = "data/lake/silver/ibex"
RUTA_SILVER_SENTIMIENTO = "data/lake/silver/sentimiento"
RUTA_SILVER_EMPRESAS = "data/lake/silver/empresas"

# Capa gold: datos integrados y preparados para analisis
RUTA_GOLD_HECHOS = "data/lake/gold/hechos"
RUTA_GOLD_DIM_EMPRESA = "data/lake/gold/dim_empresa"
RUTA_GOLD_DIM_FECHA = "data/lake/gold/dim_fecha"
RUTA_GOLD_HECHOS_METRICAS = "data/lake/gold/hechos_metricas"
RUTA_EXPORT_GOLD = "data/export/gold"

# Tickers utilizados para descargar las empresas del IBEX-35 desde Yahoo Finance.
TICKERS_IBEX = [
    "ANA.MC", "ANE.MC", "ACX.MC", "ACS.MC", "AENA.MC", "AMS.MC",
    "MTS.MC", "BBVA.MC", "SAB.MC", "SAN.MC", "BKT.MC", "CABK.MC",
    "CLNX.MC", "ENG.MC", "ELE.MC", "FER.MC", "FDR.MC", "GRF.MC",
    "IAG.MC", "IBE.MC", "ITX.MC", "IDR.MC", "COL.MC", "LOG.MC",
    "MAP.MC", "MRL.MC", "NTGY.MC", "PUIG.MC", "RED.MC", "REP.MC",
    "ROVI.MC", "SCYR.MC", "SLR.MC", "TEF.MC", "UNI.MC"]
