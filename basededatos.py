# -*- coding: utf-8 -*-
import sqlite3

global con
global cur

con = sqlite3.connect('datos.db')
cur = con.cursor()
from tkinter import *
from tkinter import messagebox

ventana=Tk()
global ventana_registro
global E_correon
global E_nombre
global E_apellidos
global E_ocupacion
global E_contraseñan
global E_contraseña_confirm
global ventana_perfil
global perfil
global ventana_registro2
global corr_act
global Entry_contra
global ventana_borrar

def validar():
    global cur
    global ventana_registro
    global E_correon
    global E_nombre
    global E_apellidos
    global E_ocupacion
    global E_contraseñan
    global E_contraseña_confirm
    
    correon=str(E_correon.get())
    nombre=str(E_nombre.get())
    apellidos=str(E_apellidos.get())
    ocupacion=str(E_ocupacion.get())
    contraseñan=str(E_contraseñan.get())
    contraseña_confirm=str(E_contraseña_confirm.get())
    #checar detalle con la contraseña cuando sea distinta
    if contraseñan!=contraseña_confirm:
        messagebox.showerror("Contraseñas diferentes","Revisa las contraseñas, son diferentes")
        
    else:
        cur.execute('INSERT INTO usuarios (nombre, apellidos,contraseña, correo, ocupacion) VALUES(?, ?, ?, ?, ?)', (nombre, apellidos, contraseñan, correon, ocupacion))
        messagebox.showinfo("Alta registrada","Usuario registrado")
        ventana_registro.destroy()
        con.commit()
        cur.close()

def registrar ():
    global E_correon
    global E_nombre
    global E_apellidos
    global E_ocupacion
    global E_contraseñan
    global E_contraseña_confirm
    global ventana_registro
    
    ventana_registro=Tk()
    Label_correon=Label(ventana_registro,text="Ingresa tu correo electronico\n")
    Label_nombre=Label(ventana_registro,text="Ingresa tu nombre\n")
    Label_apellidos=Label(ventana_registro,text="Ingresa tus apellidos\n")
    Label_ocupacion=Label(ventana_registro,text="¿A que te dedicas?")
    Label_contraseñan=Label(ventana_registro,text="Ingresa tu contraseña\n")
    Label_contraseña_confirm=Label(ventana_registro,text="confirma tu contraseña\n")

    E_correon=Entry(ventana_registro)
    E_nombre=Entry(ventana_registro)
    E_apellidos=Entry(ventana_registro)
    E_ocupacion=Entry(ventana_registro)
    E_contraseñan=Entry(ventana_registro)
    E_contraseña_confirm=Entry(ventana_registro)

    Label_correon.grid(row=1, column=1)
    Label_nombre.grid(row=2, column=1)
    Label_apellidos.grid(row=3, column=1)
    Label_ocupacion.grid(row=4, column=1)
    Label_contraseñan.grid(row=5, column=1)
    Label_contraseña_confirm.grid(row=6, column=1)

    E_correon.grid(row=1, column=3)
    E_nombre.grid(row=2, column=3)
    E_apellidos.grid(row=3, column=3)
    E_ocupacion.grid(row=4, column=3)
    E_contraseñan.grid(row=5, column=3)
    E_contraseña_confirm.grid(row=6, column=3)

    Val_datos=Button(ventana_registro,text="Crear usuario", command=validar)
    Val_datos.grid(row=7, column=2)

    messagebox.showinfo("informacion","Llena todos los datos, no dejes ninguno en blanco")

    ventana_registro.mainloop()


def Eliminar():
    global perfil
    global Entry_contra
    global ventana_perfil
    global ventana_borrar
    
    eliminar=str(Entry_contra.get())
    if eliminar==perfil[0]:
        cur.execute("DELETE FROM usuarios WHERE nombre ='"+eliminar+"'")
        messagebox.showinfo("Cuenta eliminada","El usuario se ha eliminado")
        con.commit()
        #con.commit()
        con.close()
        ventana_perfil.destroy()
        ventana_borrar.destroy()
        
        exit()
    else:
        messagebox.showerror("usuario no existe","Intenta de nuevo")
        
def borrar():
    global cur
    global perfil
    global Entry_contra
    global ventana_borrar
    ventana_borrar=Tk()
    label_c=Label(ventana_borrar,text="Ingresa tu nombre")
    Entry_contra=Entry(ventana_borrar)
    B_Borrar=Button(ventana_borrar,text="Eliminar",command=Eliminar)
    label_c.grid(row=1, column=1)
    Entry_contra.grid(row=2,column=1)
    B_Borrar.grid(row=3,column=1)
    ventana_borrar.mainloop()
    
    
    return contraseña
def validar_act():
    global corr_act
    global perfil
    global cur
    global con
    global ventana_registro2
    global E_correon
    global E_nombre
    global E_apellidos
    global E_ocupacion
    global E_contraseñan
    global E_contraseña_confirm
    
    correon=str(E_correon.get())
    nombre=str(E_nombre.get())
    apellidos=str(E_apellidos.get())
    ocupacion=str(E_ocupacion.get())
    contraseñan=str(E_contraseñan.get())
    contraseña_confirm=str(E_contraseña_confirm.get())
    #checar detalle con la contraseña cuando sea distinta
    if (contraseñan!=contraseña_confirm):
        messagebox.showerror("Contraseñas diferentes","Revisa las contraseñas, son diferentes\n")
                             #"No se pueden actualizar Emails, si es el caso crea otro usuario")
        
    else:
        print(perfil[3])
        sql = ("UPDATE usuarios SET nombre='"+ nombre +"',apellidos='"+apellidos+
               "',contraseña='"+contraseñan+"',ocupacion='"+ocupacion+"',correo='"+correon+"' WHERE nombre='"+perfil[0]+"'")
        print(sql)
        cur.execute(sql)
        #'UPDATE usuarios SET (nombre, apellidos,contraseña, correo, ocupacion) VALUES(?, ?, ?, ?, ?) WHERE  nombre='perfil[0]'"' (nombre, apellidos, contraseñan, correon, ocupacion))
        messagebox.showinfo("Actualizacion registrada","Información actualizada")
        con.commit()
        #
        #con.close()
        
        #con = sqlite3.connect('datos.db')
        #cur = con.cursor()
        ventana_registro2.destroy()
        cur.execute('SELECT * FROM usuarios WHERE correo = ? AND contraseña = ?',(correon,contraseñan))
        perfil = cur.fetchone()
        print(perfil)
        mostrar_perfil(perfil)
        
def Actualizar ():
    global ventana_perfil
    ventana_perfil.destroy()
    global E_correon
    global E_nombre
    global E_apellidos
    global E_ocupacion
    global E_contraseñan
    global E_contraseña_confirm
    global ventana_registro2
    global perfil
    global corr_act
    
    ventana_registro2=Tk()
    Label_correon=Label(ventana_registro2,text="Ingresa tu correo electronico\n")
    Label_nombre=Label(ventana_registro2,text="Ingresa tu nombre\n")
    Label_apellidos=Label(ventana_registro2,text="Ingresa tus apellidos\n")
    Label_ocupacion=Label(ventana_registro2,text="¿A que te dedicas?")
    Label_contraseñan=Label(ventana_registro2,text="Ingresa tu contraseña\n")
    Label_contraseña_confirm=Label(ventana_registro2,text="confirma tu contraseña\n")

    E_correon=Entry(ventana_registro2)
    E_nombre=Entry(ventana_registro2)
    E_apellidos=Entry(ventana_registro2)
    E_ocupacion=Entry(ventana_registro2)
    E_contraseñan=Entry(ventana_registro2)
    E_contraseña_confirm=Entry(ventana_registro2)

    Label_correon.grid(row=1, column=1)
    Label_nombre.grid(row=2, column=1)
    Label_apellidos.grid(row=3, column=1)
    Label_ocupacion.grid(row=4, column=1)
    Label_contraseñan.grid(row=5, column=1)
    Label_contraseña_confirm.grid(row=6, column=1)

    E_correon.grid(row=1, column=3)
    E_nombre.grid(row=2, column=3)
    E_apellidos.grid(row=3, column=3)
    E_ocupacion.grid(row=4, column=3)
    E_contraseñan.grid(row=5, column=3)
    E_contraseña_confirm.grid(row=6, column=3)

    E_correon.delete(0,END)
    E_nombre.delete(0,END)
    E_apellidos.delete(0,END)
    E_ocupacion.delete(0,END)
    E_contraseñan.delete(0,END)
    E_contraseña_confirm.delete(0,END)

    E_correon.insert(0,perfil[3])
    E_nombre.insert(0,perfil[0])
    E_apellidos.insert(0,perfil[1])
    E_ocupacion.insert(0,perfil[5])
    E_contraseñan.insert(0,perfil[2])
    E_contraseña_confirm.insert(0,perfil[2])

    

    Val_datos=Button(ventana_registro2,text="Actualizar", command=validar_act)
    Val_datos.grid(row=7, column=2)

    messagebox.showinfo("informacion","Llena todos los datos, no dejes ninguno en blanco\n")
                        

    ventana_registro2.mainloop()
def N_Python():
    global perfil
    global ventana_perfil
    import M_Python
    ventana_perfil.destroy()
    correo=perfil[3]
    contra=perfil[2]
    M_Python.test_python(correo,contra)

def N_Java():
    global perfil
    global ventana_perfil
    import M_Java
    ventana_perfil.destroy()
    correo=perfil[3]
    contra=perfil[2]
    M_Java.test_Java(correo,contra)

def N_C():
    global perfil
    global ventana_perfil
    import M_C
    ventana_perfil.destroy()
    correo=perfil[3]
    contra=perfil[2]
    M_C.test_C(correo,contra)

def N_R():
    global perfil
    global ventana_perfil
    import M_R
    ventana_perfil.destroy()
    correo=perfil[3]
    contra=perfil[2]
    M_R.test_R(correo,contra)
     

def Descubrir():
    global perfil
    global ventana_perfil
    import M_descubrete
    ventana_perfil.destroy()
    correo=perfil[3]
    contra=perfil[2]
    M_descubrete.test_descubrete(correo,contra)

def mostrar_perfil(perfil):
    global ventana_perfil
    ventana_perfil=Tk()
    ventana_perfil.geomtry=("500x500")
    ventana_perfil.config(bg="white")
    P_personales=Label(ventana_perfil,text="Datos personales \n")
    P_NOMBRE=Label(ventana_perfil,text=("Nombre \n"+str(perfil[0])+"\n"))
    P_APELLIDOS=Label(ventana_perfil,text=("Apellidos \n"+str(perfil[1])+"\n"))
    P_CORREO=Label(ventana_perfil,text=("E-mail \n"+str(perfil[3])+"\n"))
    P_OCUPACIÓN=Label(ventana_perfil,text=("Ocupación \n"+str(perfil[5])+"\n"))
    P_Niveles=Label(ventana_perfil,text="Datos Técnicos \n")
    P_NIVEL_JAVA=Label(ventana_perfil,text=("Nivel de Java \n"+str(perfil[6])+"\n"))
    P_NIVEL_PYTHON=Label(ventana_perfil,text=("Nivel de Python \n"+str(perfil[7])+"\n"))
    P_NIVEL_C=Label(ventana_perfil,text=("Nivel de C \n"+str(perfil[8])+"\n"))
    P_NIVEL_R=Label(ventana_perfil,text=("Nivel de R \n"+str(perfil[9])+"\n"))
    P_psicologicos=Label(ventana_perfil,text="Datos psicológicos \n")
    P_NIVEL_conce=Label(ventana_perfil,text=("Nivel de concentración \n"+str(perfil[10])+"\n"))
    P_NIVEL_expre=Label(ventana_perfil,text=("Nivel de expresión \n"+str(perfil[11])+"\n"))
    P_NIVEL_creat=Label(ventana_perfil,text=("Nivel de creatividad \n"+str(perfil[12])+"\n"))


    B_actualizar=Button(ventana_perfil,text="Actualizar perfil",command=Actualizar)
    B_Borrar=Button(ventana_perfil,text="Eliminar perfil" ,command=borrar)
    B_Java=Button(ventana_perfil,text="Actualizar nivel",command=N_Java)
    B_Python=Button(ventana_perfil,text="Actualizar nivel",command=N_Python)
    B_C=Button(ventana_perfil,text="Actualizar nivel",command=N_C)
    B_R=Button(ventana_perfil,text="Actualizar nivel",command=N_R)
    B_Psico=Button(ventana_perfil,text="Descubrete",command=Descubrir)
    
    P_personales.grid(row=1, column=1)
    P_NOMBRE.grid(row=2,column=2)
    P_APELLIDOS.grid(row=2 ,column= 3)
    P_CORREO.grid(row=3 ,column=2 )
    P_OCUPACIÓN.grid(row=3 ,column=3 )
    B_actualizar.grid(row=4, column=2)
    B_Borrar.grid(row=4, column=3)

    P_Niveles.grid(row=5, column=1)
    P_NIVEL_JAVA.grid(row=6 ,column=2)
    P_NIVEL_PYTHON.grid(row=6,column=3)
    B_Java.grid(row=7, column=2)
    B_Python.grid(row=7, column=3)
    P_NIVEL_C.grid(row= 8,column=2 )
    B_C.grid(row=9, column=2)
    P_NIVEL_R.grid(row=8 ,column=3 )
    B_R.grid(row=9, column=3)

    P_psicologicos.grid(row=10, column=1)
    P_NIVEL_conce.grid(row=11 ,column=2 )
    P_NIVEL_expre.grid(row=11 ,column=3 )
    P_NIVEL_creat.grid(row=12 ,column=2 )
    B_Psico.grid(row=12, column=3)

    

##    print ("NOMBRE: ",perfil[0])
##    print ("APELLIDOS: ",perfil[1])
##    print ("CORREO: ",perfil[3])
##    print ("OCUPACIÓN: ",perfil[5])
##    print ("NIVEL JAVA:",perfil[6])
##    print ("NIVEL PYTHON:",perfil[7])
##    print ("NIVEL C:",perfil[8])
##    print ("NIVEL R:",perfil[9])
##    return perfil

def Cargar():
    correos=[]
    for row in cur.execute('SELECT * FROM usuarios'):
        correos.append(str(row))
    #for row in cur.execute('SELECT correo FROM usuarios WHERE nivel = "1"'):
##        correos.append(str(row))
##    for row in cur.execute('SELECT correo FROM usuarios WHERE nivel = "2"'):
##        correos.append(str(row))
    print(correos)

    Em=Spinbox(ventana,values=correos)
    Em.grid(row=8,column=1)

def ver_perfiles():
    print("Ellos son usuarios")
    for row in cur.execute('SELECT * FROM usuarios WHERE nivel = "0"'):
        print(row)
    print("Ellos son empresarios")
    for row in cur.execute('SELECT nombre FROM usuarios WHERE nivel = "1"'):
        print(row)    
##    print("Ellos son administradores")
##    for row in cur.execute('SELECT nombre FROM usuarios WHERE nivel = "2"'):
##        print(row)    
##    for row in cur.execute("SELECT correo FROM usuarios WHERE java = 'correo' "):
##        print(row)

def tabla_Niveles():
    print("Niveles")
    Niveles=[]
    for row in cur.execute('SELECT nombre,apellidos,python,c,r,java FROM usuarios'):
        Niveles.append(str(row)+'\n')
    print("Nombre | Apellidos | Niv Python | Niv C | Niv r | Niv java")
    print(Niveles)

    
def tabla_Psic():
    print("Psic")
    Psic=[]
    for row in cur.execute('SELECT nombre,apellidos,concentracion,expresion,creatividad FROM usuarios'):
        Psic.append(str(row)+'\n')
    print("Nombre | Apellidos | concentracion | expresion | creatividad")
    print(Psic)
    
def tabla_Con():
    print("Concentrado")
    Todo=[]
    for row in cur.execute('SELECT nombre,apellidos,python,c,r,java,concentracion,expresion,creatividad FROM usuarios'):
        Todo.append(str(row)+'\n')
    print("Nombre | Apellidos | Niv Python | Niv C | Niv r | Niv java |concentracion | expresion | creatividad")
    print(Todo)
    
    
def Empresa_perfil(perfil):
    print("Empresa")
    global ventana_perfil
    ventana_perfil=Tk()
    ventana_perfil.geomtry=("500x500")
    ventana_perfil.config(bg="white")
    
    L_personales=Label(ventana_perfil,text="Datos personales \n")
    L_NOMBRE=Label(ventana_perfil,text=("Nombre \n"+str(perfil[0])+"\n"))
    L_CORREO=Label(ventana_perfil,text=("E-mail \n"+str(perfil[3])+"\n"))
    
    L_Niveles=Label(ventana_perfil,text="Datos Técnicos \n")              
    L_psicologicos=Label(ventana_perfil,text="Datos psicológicos \n")
    L_Concentrado=Label(ventana_perfil,text=("Concentrado de datos \n"+str(perfil[12])+"\n"))


    B_actualizar=Button(ventana_perfil,text="Actualizar perfiles")#,command=Actualizar_empresa)
    B_Borrar=Button(ventana_perfil,text="Eliminar perfiles")# ,command=borrar_empresa)
    B_Niveles=Button(ventana_perfil,text="Tabla de niveles",command=tabla_Niveles)
    B_Psi=Button(ventana_perfil,text="Tabla psicolgicos",command=tabla_Psic)
    B_Concentrado=Button(ventana_perfil,text="Tabla concentrado",command=tabla_Con)
       
    L_personales.grid(row=1, column=1)
    L_NOMBRE.grid(row=2,column=2)
    L_CORREO.grid(row=2 ,column=3)

    B_actualizar.grid(row=4, column=2)
    B_Borrar.grid(row=4, column=3)

    L_Niveles.grid(row=5, column=1)
    L_psicologicos.grid(row=5,column=2)
    L_Concentrado.grid(row=5,column=3)

    B_Niveles.grid(row=6,column=1)
    B_Psi.grid(row=6,column=2)
    B_Concentrado.grid(row=6,column=3)

def boton():
    global cur
    global E_email
    global E_contra
    global perfil
    con = sqlite3.connect('datos.db')
    cur = con.cursor()
    
    correo=str(E_email.get())
    contraseña=str(E_contra.get())
    cur.execute('SELECT * FROM usuarios WHERE correo = ? AND contraseña = ?',(correo,contraseña))
    perfil = cur.fetchone()
    ocu=perfil[1]
    if (ocu!='org'):
        if perfil:
            mostrar_perfil(perfil)
            ventana.destroy()
        else:
            messagebox.showinfo("No estas registrado","No se encuentra informacion en base de datos \n"+
                                "Crea tu resgitro para acceder")
    else:
        if perfil:
            Empresa_perfil(perfil)
            ventana.destroy()
        else:
            messagebox.showinfo("No estas registrado","No se encuentra informacion en base de datos \n"+
                                "Crea tu resgitro para acceder")
        
        
    
global E_email
global E_contra

label_usuario=Label(ventana,text="Ingresa tu E-mail")
label_contra=Label(ventana,text="Ingresa tu contraseña")
E_email=Entry(ventana)
E_contra=Entry(ventana)

label_usuario.grid(row=1,column=1)
label_contra.grid(row=3,column=1)
E_email.grid(row=2,column=1)
E_contra.grid(row=4,column=1)

B_aceptar=Button(ventana,text="Aceptar",command=boton)
B_aceptar.grid(row=5, column=1)

B_Noregistro=Button(ventana,text="No estoy registrado",command=registrar)
B_Noregistro.grid(row=6, column=1)

B_cargar=Button(ventana,text="Cargar registros",command=Cargar)
B_cargar.grid(row=7, column=1)

ventana.mainloop()


    
