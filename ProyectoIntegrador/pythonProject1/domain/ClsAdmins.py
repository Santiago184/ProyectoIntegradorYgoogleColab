from ConexionSql import conexionbd

conexion = conexionbd()

class Admin:
    def __init__(self,id,nombre,apellido,rol,correo,clave):
        self._id=id
        self._nombre=nombre
        self._apellido=apellido
        self._rol=rol
        self._correo=correo
        self._clave=clave

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def telefono(self, rol):
        self._rol= rol

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def clave(self):
        return self._clave

    @clave.setter
    def clave(self, clave):
        self._clave = clave

    def CrearUsuario(self):
        self._id=int(input("Id: "))
        self._nombre=input("Nombre: ")
        self._apellido=input("Apellido: ")
        self._rol = input("Rol: ")
        self._correo=input("Correo: ")
        self._clave=int(input("Clave: "))


    def Consultar(self,id):
        with conexion.cursor() as cursor:

            try:
                cursor=conexion.cursor()
                sql="SELECT * FROM Roles WHERE IdRol = ?"
                cursor.execute(sql,(id))
                result=cursor.fetchone()
                if result:
                    info={
                        "id": result.IdRol,
                        "nombre": result.NombreRol,
                        "apellido": result.ApellidoRol,
                        "rol": result.Rol,
                        "correo": result.Correo
                    }
                    return info
                else:

                    print("Usuario no encontrado")
            except Exception as e:
                print("Error al consultar",e)


    def InisiarA(self,correo,clave):
        with conexion.cursor() as cursor:

            try:
                cursor=conexion.cursor()
                sql="SELECT * FROM Roles WHERE Correo = ? AND Clave=?"
                cursor.execute(sql,(correo,clave))
                result=cursor.fetchone()
                if result:
                    info={
                        "id": result.IdRol,
                        "nombre": result.NombreRol,
                        "apellido": result.ApellidoRol,
                        "rol": result.Rol,
                        "correo": result.Correo
                    }
                    return info
                else:
                    print("Admin no encontrado")
            except Exception as e:
                print("Error al consultar",e)