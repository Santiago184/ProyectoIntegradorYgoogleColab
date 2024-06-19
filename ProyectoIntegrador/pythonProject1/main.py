import contextlib
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,HTTPException, Depends
from typing import Union
from pydantic import BaseModel
from domain.ConexionSql import conexionbd
from domain.ClsUsuario import Usuario
from domain.ClsReservas import Reserva
re=Reserva(None,None,None,None,None)
us=Usuario(None, None, None, None, None, None)
conexion=conexionbd()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@contextlib.contextmanager
def get_db():
    conn = conexionbd()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection error")
    try:
        yield conn
    finally:
        conn.close()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/{user_id}")
def read_user(user_id):
    user=us.Consultar(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
@app.post("/users")
def read_user(id, nombre, apellido, telefono, correo, clave):
    new_user=Usuario(id,nombre, apellido, telefono, correo, clave)
    new_user.Guardar()
    if not new_user:
        raise HTTPException(status_code=404, detail="User not found")
    return new_user

@app.post("/reserva")
def read_res(destino, fecha, dias, npersonas, valor):
    new_res=Reserva(destino,fecha,dias,npersonas,valor)
    new_res.Guardar()
    if not new_res:
        raise HTTPException(status_code=404, detail="User not found")
    return new_res

@app.get("/login")
def login(correo: str ,clave : str):
    user=us.InisiarU(correo,clave)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

