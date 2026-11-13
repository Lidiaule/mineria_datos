class ConexionJDBC:
    # Guarda los parametros necesarios para que Spark pueda escribir en MySQL por JDBC

    def __init__(self, host="localhost:3306", database="IBEX35", user="root", password="1234"):
        # Datos basicos de la conexion
        self._host = host
        self._database = database
        self._user = user
        self._password = password

        # URL JDBC en el formato utilizado por MySQL
        self._url = (
            f"jdbc:mysql://{self._host}/{self._database}"
            f"?useSSL=false"
            f"&allowPublicKeyRetrieval=true"
            f"&serverTimezone=UTC")

        # Driver JDBC de MySQL
        self._driver = "com.mysql.cj.jdbc.Driver"

    def get_url(self):
        # Devuelve la URL JDBC
        return self._url

    def get_propiedades(self):
        # Devuelve las propiedades que necesita df.write.jdbc()
        return {
            "user": self._user,
            "password": self._password,
            "driver": self._driver}
