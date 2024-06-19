Create database viajes

Use viajes

Create table Roles(
IdRol int primary key,
NombreRol varchar(100),
ApellidoRol varchar(100),
Rol varchar(100),
Correo varchar(100),
Clave int)
insert into Roles values (150,'santiago','posada','administrador','admin@correo.com',1234)
SELECT * FROM Roles WHERE Correo = 'admin@correo.com'
--tabla usuario
Create table Usuario(
IdUs int  primary key,
NombreUs varchar (80),
ApellidoUs varchar (80),
Telefono varchar(15), 
Correo varchar (80),
Clave int)


create table Destino(
CodDe int primary key identity,
NombreDe varchar (100))

Create table Reserva(
CodRe int primary key identity,
Destino varchar(80),
fechaRe varchar (20),
Dias int,
Npersonas int ,
valor float
)

select * from Roles
select * from Usuario 
select * from Destino
select * from Reserva
delete From Usuario where IdUs='1000123456'
update Usuario set NombreUs='santi' where IdUs='1000123456'

