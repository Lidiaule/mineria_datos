from src.modelo.conexion.SparkSession import SparkSessionPractica
from src.modelo.conexion.ConexionJDBC import ConexionJDBC
from src.modelo.conexion.GuardarDatos import GuardarDatos

from src.modelo.ejercicios.practica0 import Ejercicio1
from src.modelo.ejercicios.practica0_2 import Ejercicio2
from src.modelo.ejercicios.practica0_3 import Ejercicio3
from src.modelo.ejercicios.practica0_4 import Ejercicio4
from src.modelo.ejercicios.practica0_5 import Ejercicio5
from src.modelo.ejercicios.practica0_6 import Ejercicio6


class Controlador:

    def __init__(self, path_csv="./data/ibex35.csv"):
        self.path_csv = path_csv
        self.spark = SparkSessionPractica.crear_sesion()
        self.df = None

    def ejecutar_practica(self):
        # Ejercicio 1
        ej1 = Ejercicio1(self.spark, self.path_csv)
        self.df = ej1.apartado_a()
        self.df = ej1.apartado_b(self.df)
        df_schema_custom = ej1.apartado_c()

        # Ejercicio 2
        ej2 = Ejercicio2()
        self.df, filas_eliminadas, num_empresas = ej2.apartado_a(self.df)
        fecha_inicio, fecha_fin, dias = ej2.apartado_b(self.df)

        # Ejercicio 3
        ej3 = Ejercicio3()
        self.df, resultados_stats = ej3.apartado_a(self.df)
        self.df = ej3.deficiency_notice(self.df)
        ej3.apartado_b()

        # Ejercicio 4
        ej4 = Ejercicio4()
        df_variacion = ej4.ejecutar(self.df)

        # Ejercicio 5
        ej5 = Ejercicio5()
        self.df = ej5.ejecutar(self.df)
        df_aena_bbva = ej5.obtener_aena_bbva(self.df)

        # Ejercicio 6
        ej6 = Ejercicio6()
        self.df = ej6.ejecutar(self.df)

    def guardar_en_bd(self, host="localhost", database="IBEX35", user="root", password="1234", tabla="ibex35_procesado"):
        conexion = ConexionJDBC(
            host=host,
            database=database,
            user=user,
            password=password
        )
        guardar_servicio = GuardarDatos(conexion)
        guardar_servicio.guardar(self.df, tabla=tabla)
        
    def cerrar_sesion(self):
        if self.spark:
            self.spark.stop()