from src.modelo.conexion.SparkSession import SparkSessionPractica

from src.modelo.ejercicios.Ejercicio1A import Ejercicio1A
from src.modelo.ejercicios.Ejercicio1B import Ejercicio1B
from src.modelo.ejercicios.Ejercicio1C import Ejercicio1C
from src.modelo.ejercicios.Ejercicio2A import Ejercicio2A
from src.modelo.ejercicios.Ejercicio2B import Ejercicio2B
from src.modelo.ejercicios.Ejercicio2C import Ejercicio2C
from src.modelo.ejercicios.Ejercicio3 import Ejercicio3
from src.modelo.ejercicios.Ejercicio4 import Ejercicio4
from src.modelo.ejercicios.Ejercicio5A import Ejercicio5A
from src.modelo.ejercicios.Ejercicio5B import Ejercicio5B
from src.modelo.ejercicios.Ejercicio5C import Ejercicio5C
from src.modelo.ejercicios.Ejercicio5D import Ejercicio5D
from src.modelo.ejercicios.Ejercicio6 import Ejercicio6
from src.modelo.ejercicios.Ejercicio7 import Ejercicio7
from src.modelo.ejercicios.Ejercicio8 import Ejercicio8
from src.modelo.ejercicios.Ejercicio9 import Ejercicio9
from src.modelo.ejercicios.Ejercicio10 import Ejercicio10
from src.modelo.ejercicios.Ejercicio11 import Ejercicio11
from src.modelo.ejercicios.Ejercicio12 import Ejercicio12
from src.modelo.ejercicios.Ejercicio13 import Ejercicio13



class Controlador:

    def __init__(self):
        # Usamos la SparkSession
        self.spark = SparkSessionPractica.crear_sesion()

    def ejecutar_practica(self):
        
        Ejercicio1A(self.spark).ejecutar("IBE.MC", "2024-10-01", "2026-10-02")
        Ejercicio1B(self.spark).ejecutar()
        Ejercicio1C(self.spark).ejecutar()

        # Guardamos el Dataframe
        df_sentimiento = Ejercicio2A(self.spark).ejecutar()
        Ejercicio2B().ejecutar(df_sentimiento)
        Ejercicio2C(self.spark).ejecutar(df_sentimiento)

        Ejercicio3(self.spark).ejecutar()

        # Guardamos la versión final del Ej4 
        version_ejercicio4 = Ejercicio4(self.spark).ejecutar()

        # Guardamos la versión anterior a 5A para poder leerla después con versionAsOf
        version_antes_5a = Ejercicio5A(self.spark).ejecutar()
        Ejercicio5B(self.spark).ejecutar()
        Ejercicio5C(self.spark).ejecutar()
        Ejercicio5D(self.spark).ejecutar(version_antes_5a, version_ejercicio4)

        # RESTORE deja realmente la tabla como estaba al terminar el Ej4
        Ejercicio6(self.spark).ejecutar(version_ejercicio4)

        Ejercicio7(self.spark).ejecutar()
        Ejercicio8(self.spark).ejecutar()
        Ejercicio9(self.spark).ejecutar()
        Ejercicio10(self.spark).ejecutar()
        Ejercicio11(self.spark).ejecutar()
        Ejercicio12(self.spark).ejecutar()
        Ejercicio13(self.spark).ejecutar()

    def cerrar_sesion(self):
        # Cerramos Spark 
        if self.spark:
            self.spark.stop()
