# -*- coding: cp1252 -*-
#Modulo de R
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
   total=8
   V=(float(sum(cal))/total)*10.0
   Labelfin=Label(ventana,text="Has llegado al fina de la prueba \n"+
                  "Felididades por intentar mejorar siempre.\n"+
                  "Nunca te rindas, tu puntaje obtenido es" )
   Calif=Label(ventana,text=(str(V)+" Puntos"))
   Labelfin.grid(row=1, column=1)
   Calif.grid(row=2,column=1)
   sql = ("UPDATE usuarios SET java='"+str(V)+"' WHERE correo='"+user+"'")
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
   if (res1=='25,27, 29, 31'):
      cal.append(1)
      #print("Bien hecho")
   else:
      cal.append(0)  
  
   ventana.destroy()

def Validar7 ():
   global cal
   global ventana
   global x
   global E1

   res1=str(E1.get())
   if (res1=='29'):
      cal.append(1)
      #print("Bien hecho")
   else:
      cal.append(0)  
  
   ventana.destroy()

def Validar6 ():
   global cal
   global ventana
   global x
   global E1
#11_8_1_4_6_3_7_9_10_2
   res1=str(E1.get())
   if ((res1=='11_8_1_4_6_3_7_9_10_2')or(res1=='11_8_4_1_6_3_7_9_10_2')):
      cal.append(1)
      #print("Bien hecho")
   else:
      cal.append(0)  
  
   ventana.destroy()

def Validar5 ():
   global cal
   global ventana
   global x
   global E1

   res1=str(E1.get())
   if (res1=='No es bisiesto'):
      cal.append(1)
      #print("Bien hecho")
   else:
      cal.append(0) 
  
   ventana.destroy()

def Validar4 ():
   global cal
   global ventana
   global x
   global E1

   res1=str(E1.get())
   if (res1=="3,11,8,4,9,7,1,2,5,6,10"):
      cal.append(1)
      #print("Bien hecho")
   else:
      cal.append(0)

  
   ventana.destroy()

def Validar3 ():
   global cal
   global ventana
   global x
   global E1
   res1=str(E1.get())
   
   if (res1=="Hack"):
      cal.append(1)
      #print("Bien hecho")
   else:
      cal.append(0)
  
   ventana.destroy()

def Validar2 ():
   global cal
   global ventana
   global x
   global E1
   
   res=str(E1.get())
   if (res=="15"):
      cal.append(1)
      #print("Bien hecho")
   else:
      cal.append(0)
  
   ventana.destroy()

def Validar ():
   global cal
   global ventana
   global Nivel
   global x
   global E1
   global Im1

   res=(str(E1.get()))
   
   if (res=="81"):
      cal.append(1)
      #print("Bien hecho")
   else:
      cal.append(0)
#      print("Buen intento")
  
   ventana.destroy()
def test_Java(user,contra):
   global cal
   global ventana
   cal=[]
   ventana= Tk()
   ventana.geometry=("600x500")
   ventana.title("Test de Java")
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
            
            N11 = ImageTk.PhotoImage(Image.open("J_N1.gif"))
            instr=Label(ventana,text='Indica el resultado \n'+
                        'que se muestra al ejecutar este código')
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
            
            instr=Label(ventana,text='Escribe el resultado \n'+
                        'que se obtiene al ejecutar el código')
            instr.grid(row=1, column=1)
            
            N21 = ImageTk.PhotoImage(Image.open("J_N2.gif"))
            
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
            
            N31 = ImageTk.PhotoImage(Image.open("J_N3.gif"))
            
            E1=Entry(ventana)
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
            N41 = ImageTk.PhotoImage(Image.open("J_N4.gif"))
            # 3,11,8,(4 o 9),(4 o 9),7,1,2,5,6,10
            Vector=["8,1,5,9,4,3,7,2,6,10","3,11,8,4,9,7,1,2,5,6,10","4,11,3,8,10,7,1,2,5,6,9"]
            E1=Spinbox(ventana,values=Vector)
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
            N51 = ImageTk.PhotoImage(Image.open("J_N5.gif"))
            Vector=[" ","Bisiesto","No es bisiesto"]
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
            instr=Label(ventana,text='Ordena los numeros de código para \n'+
                        'obtener un factorial de orden 5 \n'+
                        'separados por un _ ejemplo 1_2_3_4...')
            instr.grid(row=1, column=1)
            
            N61 = ImageTk.PhotoImage(Image.open("J_N6.gif"))
            
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
            instr=Label(ventana,text='Indica la cantidad de numeros que se imprimen')
            instr.grid(row=1, column=1)
            N71 = ImageTk.PhotoImage(Image.open("J_N7.gif"))
            
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
            instr=Label(ventana,text='Ingresa los valores que  \n'+
                        'se imprimen separados por una "," ejemplo \n' +
                        '1,2,3,4,5' )
            instr.grid(row=1, column=1)
            N81 = ImageTk.PhotoImage(Image.open("J_N8.gif"))
            #_25,27, 29, 31
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
      if (Nivel==8):
         ventana.mainloop()
      
      #except:
