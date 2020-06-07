# -*- coding: utf-8 -*-
import sqlite3
con = sqlite3.connect("datos.db")
cur = con.cursor()

def mostrar_perfil(perfil):
    print ("NOMBRE: ",perfil[0])
    print ("APELLIDOS: ",perfil[1])
    print ("CORREO: ",perfil[2])
    print ("empresa: ",perfil[3])
    print ("ambiente laboral:",perfil[4])
    return perfil

def inicio():
    
    correo=str(input("Ingresa tu E-mail \n"))
    contraseña=str(input("Ingresa tu contraseña \n"))
 
    cur.execute('SELECT * FROM empresas WHERE correo = ? AND contraseña = ?',(correo,contraseña))
    perfil = cur.fetchone()

    if perfil:
        mostrar_perfil(perfil)
    else:
        print("No estás registrado!\n registrate")
    
def registrar ():
    correon=str(input("Ingresa tu correo electronico\n"))
    nombre=str(input("Ingresa tu nombre\n"))
    apellidos=str(input("Ingresa tus apellidos\n"))
    empresa=str(input("¿A que te dedicas?"))
    contraseñan=str(input("Ingresa tu contraseña\n"))
    contraseña_confirm=str(input("confirma tu contraseña\n"))
    #checar detalle con la contraseña cuando sea distinta
    if contraseñan!=contraseña_confirm:
        print("Las contraseñas no son iguales")
    else:
        cur.execute('INSERT INTO usuarios (nombre, apellidos, correo, empresa, contraseña) VALUES(?, ?, ?, ?, ?)', (nombre, apellidos, correo, empresa, contraseña))

def publicarvacantes ():
    vacantes = str(input("Ingresa el nombre de tu vacante"))
    cur.execute('INSERT INTO vacantes (vacante, empresavacante) value(?,?)',vacantes, empresavac)

def borrarvacantes ():
    eliminar=str(input("Ingresa el nombre de la vacante que deseas dar de baja"))
    cur.execute('DELETE FROM vacantes WHERE nombrevacante = ?', (eliminar,))

def borrar(perfil):
    eliminar=str(input("Si deseas eliminar tu cuenta ingresa tu contraseña \n"))
    if eliminar==perfil[2]:
        print("Eliminada con exito")
        cur.execute('DELETE FROM usuarios WHERE contraseña = ?', (eliminar,))
    else:
        print("Contraseña invalida")

def perfilordenadosleng():
    leng = str(input("Ingresa el lenguaje que buscas"))
    if leng=='c':
        cur.execute('SELECT nombre,apellidos,correo,ocupacion, java, python, r, c FROM usuarios ORDER BY c DESC')
        myresult = cur.fetchall()
        print("nombre       |apellidos      |correo                      | ocupacion|java|python|r|c")
        for x in myresult:
            print("|",x,"|")
    if leng=='java':
        cur.execute('SELECT nombre,apellidos,correo,ocupacion, java, python, r, c FROM usuarios ORDER BY java DESC')
        myresult = cur.fetchall()
        print("nombre       |apellidos      |correo                      | ocupacion|java|python|r|c")
        for x in myresult:
            print("|",x,"|") 
    if leng=='python':
        cur.execute('SELECT nombre,apellidos,correo,ocupacion, java, python, r, c FROM usuarios ORDER BY python DESC')
        myresult = cur.fetchall()
        print("nombre       |apellidos      |correo                      | ocupacion|java|python|r|c")
        for x in myresult:
            print("|",x,"|")
    if leng=='r':
        cur.execute('SELECT nombre,apellidos,correo,ocupacion, java, python, r, c FROM usuarios ORDER BY r DESC')
        myresult = cur.fetchall()
        print("nombre       |apellidos      |correo                      | ocupacion|java|python|r|c")
        for x in myresult:
            print("|",x,"|")
def perfilordenadosapt():
    apt = str(input("Ingresa el lenguaje que buscas"))
    if apt=='conc':
        cur.execute('SELECT nombre,apellidos,correo,ocupacion, concentracion, expresion, creatividad FROM usuarios ORDER BY cocentracion DESC')
        myresult = cur.fetchall()
        print("nombre       |apellidos      |correo                      | ocupacion|concentracion|expresion|creatividad")
        for x in myresult:
            print("|",x,"|")
    if apt=='exp':
        cur.execute('SELECT nombre,apellidos,correo,ocupacion, concentracion, expresion, creatividad FROM usuarios ORDER BY expresion DESC')
        myresult = cur.fetchall()
        print("nombre       |apellidos      |correo                      | ocupacion|concentracion|expresion|creatividad")
        for x in myresult:
            print("|",x,"|") 
    if apt=='crea':
        cur.execute('SELECT nombre,apellidos,correo,ocupacion, concentracion, expresion, creatividad FROM usuarios ORDER BY creatividad DESC')
        myresult = cur.fetchall()
        print("nombre       |apellidos      |correo                      | ocupacion|concentracion|expresion|creatividad")
        for x in myresult:
            print("|",x,"|")
    