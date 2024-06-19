from domain.ConexionSql import conexionbd

conexion = conexionbd()

class Reserva:
    def __init__(self,destino,fecha,dias,npersonas,valor):
        self._destino=destino
        self._fecha=fecha
        self._dias=dias
        self._npersonas=npersonas
        self._valor=valor

    @property
    def destino(self):
        return self._destino

    @destino.setter
    def destino(self, destino):
        self._destino = destino

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def dias(self):
        return self._dias

    @dias.setter
    def dias(self, dias):
        self._dias = dias

    @property
    def npersonas(self):
        return self._npersonas

    @npersonas.setter
    def npersonas(self, npersonas):
        self._npersonas = npersonas

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    def CrearUsuario(self):
        self._destino=int(input("Destino: "))
        self._fecha=input("Fecha: ")
        self._dias=input("Dias: ")
        self._npersonas = input("Npersonas: ")
        self._valor=input("valor: ")


    def Guardar(self):

        with conexion.cursor() as cursor:
            try:
                cursor=conexion.cursor()

                sql = "INSERT INTO Reserva (Destino,fechaRe,Dias,Npersonas,valor) VALUES (?, ?, ?, ?,?)"
                cursor.execute(sql, (self._destino,self._fecha,self._dias,self._npersonas,self._valor))
                conexion.commit()
                print("Datos insertados")

            except Exception as e:
                print("Error al insertar",e)