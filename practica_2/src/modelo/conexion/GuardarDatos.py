class GuardarDatos:
    # Guardar un DataFrame de Spark en una tabla MySQL

    def __init__(self, conexion):
        self.conexion = conexion

    def guardar(self, df, tabla="Datos2024"):
        try:
            # write.jdbc recibe la URL, nombre de tabla, modo y propiedades de conexion
            df.write.jdbc(
                url=self.conexion.get_url(),
                table=tabla,
                mode="overwrite",
                properties=self.conexion.get_propiedades())

            print("Datos guardados correctamente en la base de datos.")

        except Exception as e:
            # Mostramos el error 
            print("Error guardando los datos:", e)
