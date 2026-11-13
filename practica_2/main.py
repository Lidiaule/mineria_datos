from src.controlador.Controlador import Controlador

def main():
    # El main solo crea el controlador y arranca la practica
    controlador = Controlador()

    try:
        controlador.ejecutar_practica()
    finally:
        # finally garantiza que Spark se cierre aunque ocurra un error durante un ejercicio
        controlador.cerrar_sesion()


if __name__ == "__main__":
    main()
