# -*- coding: cp1252 -*-
#Modulo de C
from tkinter import *
from tkinter import messagebox
#import tkMessageBox
from PIL import ImageTk, Image
import numpy as np
global x
global E1
global E2
global E3
global E4
global E5
global Nivel
global ventana
global ventana2
global ventana3
global Im1
global Im2
global Im3
global Im4
global cal
def salir():
   global ventana
   exit()
def final(user,contra):
   import sqlite3
   global perfil
   global cal
   global ventana
   print(user)
   con = sqlite3.connect('datos.db')
   cur = con.cursor()
   cur.execute('SELECT * FROM usuarios WHERE correo = ? AND contraseña = ? ',(user,contra))
   perfil = cur.fetchone()
   
   ventana= Tk()
   ventana.geometry=("600x500")
   ventana.title("Resultados de python")
   ventana.config(bg="yellow")
   ventana.attributes("-topmost", True)
   total=8.0
   V=(float(sum(cal))/total)*10.0
   Labelfin=Label(ventana,text="Has llegado al fina de la prueba \n"+
                  "Felididades por intentar mejorar siempre.\n"+
                  "Nunca te rindas, tu puntaje obtenido es" )
   Calif=Label(ventana,text=(str(V)+" Puntos"))
   Labelfin.grid(row=1, column=1)
   Calif.grid(row=2,column=1)
   sql = ("UPDATE usuarios SET c='"+str(V)+"' WHERE correo='"+user+"'")
   print(sql)
   cur.execute(sql)
   #'UPDATE usuarios SET (nombre, apellidos,contraseña, correo, ocupacion) VALUES(?, ?, ?, ?, ?) WHERE  nombre='perfil[0]'"' (nombre, apellidos, contraseñan, correon, ocupacion))
   messagebox.showinfo("Actualizacion registrada","Información actualizada")
   
   con.commit()
   con.close()
  
   cerrar=Button(ventana,text="Ok",command=salir)
   cerrar.grid(row=3,column=1)
   ventana.mainloop()

def Validar8 ():
   global ventana
   global x
   global E1
   global cal

   res1=str(E1.get())
   if (res1=='-12'):
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)  
  
   ventana.destroy()

def Validar7 ():
   global cal
   global ventana
   global x
   global E1

   res1=str(E1.get())
   if (res1=='75'):
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)  
  
   ventana.destroy()

def Validar6 ():
   global cal
   global ventana
   global x
   global E1

   res1=str(E1.get())
   if (res1=='10'):
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)  
  
   ventana.destroy()

def Validar5 ():
   global cal
   global ventana
   global x
   global E1

   res1=str(E1.get())
   if (res1=='4,2,0,-2,-4,-6'):
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)  
  
   ventana.destroy()

def Validar4 ():
   global cal
   global ventana
   global x
   global E1

   res1=str(E1.get())
   if ((res1=="9") or (res1=="Nueve")):
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)

  
   ventana.destroy()

def Validar3 ():
   global cal
   global ventana
   global x
   global E1
   res1=str(E1.get())
   
   if (res1=="El valor a entrado"):
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)
  
   ventana.destroy()

def Validar2 ():
   global cal
   global ventana
   global x
   global E1
   
   res=str(E1.get())
   if ((res=='ñ')or (res=='Ñ')):
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)
  
   ventana.destroy()

def Validar ():
   global cal
   global ventana
   global Nivel
   global x
   global E1
   global Im1

   res=(int(E1.get()))
   
   if (res==29):
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)
  
   ventana.destroy()
def test_C(user,contra):
   global cal
   cal=[]
   global ventana
   ventana= Tk()
   ventana.geometry=("600x500")
   ventana.title("Test de C")
   ventana.config(bg="yellow")
   ventana.attributes("-topmost", True)
   messagebox.showinfo('Instrucciones',"Sigue lo que se indica en cada nivel")

   #tkMessageBox.showinfo('Instrucciones',"Selecciona el orden de los siguientes \n" +
    #                     "fragmentos de programas")
   
#   tkMessageBox.info('Sigue las intrucciones y \n realiza lo que se pide')
   global Nivel
   Nivel=0
   while (1):
      global x
      global E1
      global E2
      global E3
      global E4
      global E5
      global Im1
      global Im2
      global Im3
      global Im4
      #import Niveles
      if (1):
      #try:
         
         Nivel=Nivel+1
         if (Nivel==1):
            
            N11 = ImageTk.PhotoImage(Image.open("Nivel1.gif"))
            instr=Label(ventana,text='Indica el resultado \n'+
                        'del siguiente código')
            instr.grid(row=1, column=1)
            E1=Entry(ventana)
            E1.grid(row=3, column=1)
            
            
            Im1= Button(ventana, image=N11)
            Im1.grid(row=2, column=1)
           
            B_val=Button(ventana,text="Aceptar",command=Validar)
            B_val.grid(row=4,column=1)

         elif (Nivel==2):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            
            instr=Label(ventana,text='Indica que caracter \n'+
                        'produce el error de compilación')
            instr.grid(row=1, column=1)
            
            N21 = ImageTk.PhotoImage(Image.open("Nivel2.gif"))
            
            E1=Entry(ventana)
            E1.grid(row=3, column=1)
            
            
            Im1= Button(ventana, image=N21)
            Im1.grid(row=2, column=1)
           
            B_val=Button(ventana,text="Aceptar",command=Validar2)
            B_val.grid(row=4,column=1)
            pass
         
         elif (Nivel==3):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            instr=Label(ventana,text='Indica el valor de \n'+
                        'salida del siguiente código')
            instr.grid(row=1, column=1)
            
            N31 = ImageTk.PhotoImage(Image.open("Nivel3.gif"))
            valores=["","El valor a entrado","El valor no a entrado"]
            E1=Spinbox(ventana,values=valores)
            E1.grid(row=3, column=1)
            
            
            Im1= Button(ventana, image=N31)
            Im1.grid(row=2, column=1)
           
            B_val=Button(ventana,text="Aceptar",command=Validar3)
            B_val.grid(row=4,column=1)
            pass
         
         elif (Nivel==4):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            instr=Label(ventana,text='Indica el valor \n'+
                        'salida del siguiente código')
            instr.grid(row=1, column=1)
            N41 = ImageTk.PhotoImage(Image.open("Nivel4.gif"))
            
            E1=Entry(ventana)
            E1.grid(row=3, column=1)
            
            
            Im1= Button(ventana, image=N41)
            Im1.grid(row=2, column=1)
           
            B_val=Button(ventana,text="Aceptar",command=Validar4)
            B_val.grid(row=4,column=1)
            pass
         
         elif (Nivel==5):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            instr=Label(ventana,text='Indica el valor de \n'+
                        'salida del siguiente código')
            instr.grid(row=1, column=1)
            N51 = ImageTk.PhotoImage(Image.open("Nivel5.gif"))
            Vector=["6,3,5,-2,-4,-6","3,2,5,0,-4,-6","4,1,5,-2,-4,-6","4,2,0,-2,-4,-6"]
            E1=Spinbox(ventana,values=Vector)
            E1.grid(row=3, column=1)
            
            
            
            Im1= Button(ventana, image=N51)
            Im1.grid(row=2, column=1)
           
            B_val=Button(ventana,text="Aceptar",command=Validar5)
            B_val.grid(row=4,column=1)
            pass
         
         elif (Nivel==6):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            instr=Label(ventana,text='Indica el valor final \n'+
                        'salida del siguiente código')
            instr.grid(row=1, column=1)
            
            N61 = ImageTk.PhotoImage(Image.open("Nivel6.gif"))
            
            E1=Entry(ventana)
            E1.grid(row=3, column=1)
            
            
            
            Im1= Button(ventana, image=N61)
            Im1.grid(row=2, column=1)
           
            B_val=Button(ventana,text="Aceptar",command=Validar6)
            B_val.grid(row=4,column=1)
            pass
         
         elif (Nivel==7):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            instr=Label(ventana,text='Indica el valor gastado')
            instr.grid(row=1, column=1)
            N71 = ImageTk.PhotoImage(Image.open("Nivel7.gif"))
            
            E1=Entry(ventana)
            E1.grid(row=3, column=1)
            
            
            
            Im1= Button(ventana, image=N71)
            Im1.grid(row=2, column=1)
           
            B_val=Button(ventana,text="Aceptar",command=Validar7)
            B_val.grid(row=4,column=1)
            pass
         elif (Nivel==8):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            instr=Label(ventana,text='Indica el valor de \n'+
                        'salida del siguiente código')
            instr.grid(row=1, column=1)
            N81 = ImageTk.PhotoImage(Image.open("Nivel8.gif"))
            
            E1=Entry(ventana)
            E1.grid(row=3, column=1)
            
            
            
            Im1= Button(ventana, image=N81)
            Im1.grid(row=2, column=1)
           
            B_val=Button(ventana,text="Aceptar",command=Validar8)
            B_val.grid(row=4,column=1)
            pass
         elif (Nivel==9):
            final(user,contra)
      if (Nivel==1):
         ventana.mainloop()
      if (Nivel==2):
         ventana.mainloop()
      if (Nivel==3):
         ventana.mainloop()
      if (Nivel==4):
         ventana.mainloop()
      if (Nivel==5):
         ventana.mainloop()
      if (Nivel==6):
         ventana.mainloop()
      if (Nivel==7):
         ventana.mainloop()
      if (Nivel==8):
         ventana.mainloop()
      if (Nivel==9):
         ventana.mainloop()
      #except:
