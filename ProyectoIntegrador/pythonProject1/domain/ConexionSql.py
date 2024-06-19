import pyodbc

#crear variables de conexion
def conexionbd():
    server='DESKTOP-TJL429J'
    bd='viajes'
    user='Python'
    password='root1'

    try:
        conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password)
        print("Conexion Exitosa")
        return conexion
    except Exception as e:
        print("Error al intentar conectarse",e)
        return None
