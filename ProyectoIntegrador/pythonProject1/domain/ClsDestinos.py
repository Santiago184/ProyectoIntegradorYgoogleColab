from ConexionSql import conexionbd

conexion = conexionbd()

class Destino:
    def __init__(self,destino):
        self._destino=destino

    @property
    def destino(self):
        return self._destino

    @destino.setter
    def destino(self, destino):
        self._destino = destino
