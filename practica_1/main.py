from src.controlador.Controlador import Controlador


def main():
    controlador = Controlador(path_csv="./data/ibex35.csv")
    
    try:
        controlador.ejecutar_practica()
        controlador.guardar_en_bd(
            host="localhost",
            database="IBEX35",
            user="root",
            password="1234",
            tabla="ibex35_procesado"
        )
    finally:
        controlador.cerrar_sesion()


if __name__ == "__main__":
    main()