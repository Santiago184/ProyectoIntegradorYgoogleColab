from domain.ConexionSql import conexionbd

conexion = conexionbd()

class Usuario:
    def __init__(self,id,nombre,apellido,telefono,correo,clave):
        self._id=id
        self._nombre=nombre
        self._apellido=apellido
        self._telefono=telefono
        self._correo=correo
        self._clave=clave

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id=id

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido=apellido

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

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
    def clave(self,clave):
        self._clave=clave



    def CrearUsuario(self):
        self._id=int(input("Id: "))
        self._nombre=input("Nombre: ")
        self._apellido=input("Apellido: ")
        self._telefono = input("Telefono: ")
        self._correo=input("Correo: ")
        self._clave=int(input("Clave: "))


    def Guardar(self):

        with conexion.cursor() as cursor:
            try:
                cursor=conexion.cursor()
                sql = "SELECT * FROM Usuario WHERE Correo =?"
                cursor.execute(sql, (self._correo))
                result = cursor.fetchone()
                if not result:
                    sql = "INSERT INTO Usuario (IdUs,NombreUs,ApellidoUs,Telefono,Correo,Clave) VALUES (?, ?, ?, ?,?,?)"
                    cursor.execute(sql, (self._id,self._nombre, self._apellido ,self._telefono,self._correo,self._clave))
                    conexion.commit()
                    print("Datos insertados")
                else:
                    print("usuario existente")
            except Exception as e:
                print("Error al insertar",e)

    def Consultar(self,id):
        with conexion.cursor() as cursor:

            try:
                cursor=conexion.cursor()
                sql="SELECT * FROM Usuario WHERE IdUs = ?"
                cursor.execute(sql,(id))
                result=cursor.fetchone()
                if result:
                    Usinfo={
                        "id": result.IdUs,
                        "nombre": result.NombreUs,
                        "apellido": result.ApellidoUs,
                        "telefono": result.Telefono,
                        "correo": result.Correo
                    }
                    return Usinfo
                else:

                    print("Usuario no encontrado")
            except Exception as e:
                print("Error al consultar",e)



    def Eliminar(self,id):
        with conexion.cursor() as cursor:
            try:
                cursor = conexion.cursor()
                sql = "SELECT * FROM Usuario WHERE IdUs = ?"
                cursor.execute(sql, (id))
                result = cursor.fetchone()
                if result:
                    sql = "DELETE FROM Usuario WHERE IdUs = ?"
                    cursor.execute(sql, (id))
                    conexion.commit()
                    print("Usuario eliminado")
                else:
                    print("Usuario no encontrado")
            except Exception as e:
                print("Error al eliminar",e)

    def Editar(self,id):
        with conexion.cursor() as cursor:
            try:
                sql = "SELECT * FROM Usuario WHERE IdUs = ?"
                cursor.execute(sql, (id,))
                result = cursor.fetchone()
                if result:
                    self._id = result.IdUs
                    self._nombre = result.NombreUs
                    self._apellido = result.ApellidoUs
                    self._telefono = result.Telefono
                    self._correo = result.Correo
                    print("Usuario encontrado. Seleccione el campo que desea editar:")
                    print("1. Nombre")
                    print("2. Apellido")
                    print("3. Teléfono")
                    print("4. Correo")
                    opcion = input("Opción: ")

                    if opcion == "1":
                        self._nombre = input("Nuevo nombre: ")
                    elif opcion == "2":
                        self._apellido = input("Nuevo apellido: ")
                    elif opcion == "3":
                        self._correo = input("Nuevo correo: ")
                    elif opcion == "4":
                        self._telefono = input("Nuevo teléfono: ")
                    else:
                        print("Opción no válida")

                    # Actualizar el usuario en la base de datos
                    sql = "UPDATE Usuario SET NombreUs = ?, ApellidoUs = ?, Telefono = ? , Correo = ? WHERE IdUs = ?"
                    cursor.execute(sql, (self._nombre, self._apellido, self._telefono, id, self._correo))
                    conexion.commit()
                    print("Usuario actualizado")
                else:
                    print("Usuario no encontrado")
            except Exception as e:
                print("Error al editar", e)

    def InisiarU(self,correo,clave):
        with conexion.cursor() as cursor:

            try:
                cursor=conexion.cursor()
                sql="SELECT * FROM Usuario WHERE Correo = ? AND Clave=?"
                cursor.execute(sql,(correo,clave))
                result=cursor.fetchone()
                if result:
                    info={
                        "id": result.IdUs,
                        "nombre": result.NombreUs,
                        "apellido": result.ApellidoUs,
                        "telefono": result.Telefono,
                        "correo": result.Correo
                    }
                    return info
                else:
                    print("Usuario no encontrado")
            except Exception as e:
                print("Error al consultar",e)