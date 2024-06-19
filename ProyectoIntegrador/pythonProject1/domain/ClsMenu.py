from ClsUsuario import Usuario
from  ClsAdmins import Admin
from ClsReservas import Reserva
usuario=Usuario(None,None,None,None,None,None)
admin=Admin(None,None,None,None,None,None)
#reserva=Reserva("mexico","18/06/2024",8,2,5000000).Guardar()

#print(reserva)
class Menu:
    def MenuAdmin(idRol):
        menu1=True
        while(menu1):
            datos=admin.Consultar(idRol)
            nombre=datos["nombre"]
            rol=datos["rol"]
            print(f"Bienvenido {rol} {nombre}")
            op=int(input("1.Registrar\n2.Consultar\n3.Actualizar\n4.Eliminar\n0.Salir  "))
            if(op==1):
                usuario.CrearUsuario()
                usuario.Guardar()
            elif(op==2):
                id = input("Id: ")
                consulta = usuario.Consultar(id)
                print(consulta)
            elif(op==3):
                id = input("Id: ")
                usuario.Editar(id)
            elif(op==4):
                id = input("Id: ")
                usuario.Eliminar(id)
            elif(op==0):
                menu1=False
    def MenuUs(idUs):
        datos=usuario.Consultar(idUs)
        print(datos)
        menu2=True
        while menu2:
            op = int(input("1.Registrar\n2.Consultar\n3.Actualizar\n4.Eliminar\n0.Salir  "))

    menu0=True
    while(menu0):
        op = int(input("1.Inisiar como Admin\n2.Inisiar como Usuario\n0.Salir  "))
        if op==1:
            print("Inisiar como Admin")
            correo=input("Correo: ")
            clave=int(input("Clave: "))
            datos=admin.InisiarA(correo,clave)
            if datos:
                id = datos["id"]
                MenuAdmin(id)
            else:
                print("trabajador no encontrado")
        elif op==2:
            print("Inisiar como Usuario")
            correo = input("Correo: ")
            clave = int(input("Clave: "))
            datos=usuario.InisiarU(correo,clave)
            if datos:
                id = datos["id"]
                MenuUs(id)
            else:
                print("Usuario no encontrado")
        elif op==0:
            menu0=False





