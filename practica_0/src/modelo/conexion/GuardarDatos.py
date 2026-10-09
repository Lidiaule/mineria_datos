class GuardarDatos:

    def __init__(self, conexion):
        self.conexion = conexion


    def guardar(self, df, tabla="Datos2024"):

        try:
            df.write.jdbc(
                url=self.conexion.get_url(),
                table=tabla,
                mode="overwrite",
                properties=self.conexion.get_propiedades()
            )

            print("Datos guardados correctamente en la base de datos.")

        except Exception as e:
            print("Error guardando los datos:", e)