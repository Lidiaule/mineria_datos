class ConexionJDBC:

    def __init__(self, host="localhost:3306", database="IBEX35", user="root", password="1234" ):
        self._host = host
        self._database = database
        self._user = user
        self._password = password

        self._url = (
            f"jdbc:mysql://{self._host}/{self._database}"
            f"?useSSL=false"
            f"&allowPublicKeyRetrieval=true"
            f"&serverTimezone=UTC"
        )

        self._driver = "com.mysql.cj.jdbc.Driver"


    def get_url(self):
        return self._url


    def get_propiedades(self):
        return {
            "user": self._user,
            "password": self._password,
            "driver": self._driver
        }