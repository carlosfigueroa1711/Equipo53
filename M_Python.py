# -*- coding: cp1252 -*-
#Modulo de Python
from tkinter import *
from tkinter import messagebox
#import tkMessageBox
from PIL import ImageTk, Image
import numpy as np




global perfil


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
   total=17.0
   V=(float(sum(cal))/total)*10.0
   Labelfin=Label(ventana,text="Has llegado al fina de la prueba \n"+
                  "Felididades por intentar mejorar siempre.\n"+
                  "Nunca te rindas, tu puntaje obtenido es" )
   Calif=Label(ventana,text=(str(V)+" Puntos"))
   Labelfin.grid(row=1, column=1)
   Calif.grid(row=2,column=1)
   sql = ("UPDATE usuarios SET python='"+str(V)+"' WHERE correo='"+user+"'")
   print(sql)
   cur.execute(sql)
   #'UPDATE usuarios SET (nombre, apellidos,contraseña, correo, ocupacion) VALUES(?, ?, ?, ?, ?) WHERE  nombre='perfil[0]'"' (nombre, apellidos, contraseñan, correon, ocupacion))
   messagebox.showinfo("Actualizacion registrada","Información actualizada")
   
   con.commit()
   con.close()
   
   cerrar=Button(ventana,text="Ok",command=salir)
   cerrar.grid(row=3,column=1)
   ventana.mainloop()
   
               
def Validar5 ():
   global cal
   global ventana
   global x
   global E1
   global E2
   global E3

   res1=str(E1.get())
   res2=str(E2.get())
   res3=str(E3.get())
   c=0
   if (res1=='Incorrecto'):
      #print("Bien hecho")
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)
      #vector=[" ","Correcto","Incorrecto"]
   if (res2=='Correcto'):
      #print("Bien hecho")
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)
   if (res3=='Correcto'):
      #print("Bien hecho")
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
   global E2
   global E3

   res1=str(E1.get())
   res2=str(E2.get())
   res3=str(E3.get())
   c=0
   if ((res1=="1") or (res1=="TRUE") or (res1=="true") or (res1=="True")):
      #print("Bien hecho")
      cal.append(1)
   else:
      print("Buen intento")
      cal.append(0)
      
   if ((res2=="1") or (res2=="TRUE") or (res2=="true") or (res2=="True")):
      #print("Bien hecho")
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)
   if ((res3=='0') or (res3=='FALSE') or (res3=='false') or (res3=='False')):
      #print("Bien hecho")
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
   global E2
   global E3
   global E4
   global E5
   res1=[]
   res2=[]
   res1.append(int(E1.get()))
   res1.append(int(E2.get()))
   res2.append(int(E3.get()))
   res2.append(int(E4.get()))
   res3=(int(E5.get()))
   if ((res1[0]==1) and (res1[1]==1)):
      #print("Bien hecho")
      cal.append(1)
   else:
      cal.append(0)
      #print("Buen intento")
      
   if ((res2[0]==1) and (res2[1]==1)) or ((res2[0]==0) and (res2[1]==1)) or ((res2[0]==1) and (res2[1]==0)):
      #print("Bien hecho")
      cal.append(1)
   else:
      #print("Buen intento")
      cal.append(0)
   if (res3==1):
      #print("Bien hecho")
      cal.append(1)
   else:
      cal.append(0)
      #print("Buen intento")
  
   ventana.destroy()

def Validar2 ():
   global cal
   global Score
   global ventana
   global x
   global E1
   global E2
   global E3
   global E4
   res=[]
   res.append(int(E1.get()))
   res.append(int(E2.get()))
   res.append(int(E3.get()))
   res.append(int(E4.get()))
   if (np.all(x==res)):
      cal.append(4)
      #print("Bien hecho")
   elif (np.any(x==res)):
      cal.append(2)
      #print("vas bien")
   else:
      cal.append(0)
      #print("Buen intento")
  
   ventana.destroy()

def Validar ():
   global perfil
   global cal
   global ventana
   global Nivel
   global x
   global E1
   global E2
   global E3
   global E4
   global Im1
   global Im2
   global Im3
   global Im4
   global bandera
   
   res=[]
   res.append(int(E1.get()))
   res.append(int(E2.get()))
   res.append(int(E3.get()))
   res.append(int(E4.get()))
   if (np.all(x==res)):
      print("Bien hecho")
      cal.append(4)
   elif (np.any(x==res)):
      #print("vas bien")
      cal.append(2)
   else:
      #print("Buen intento")
      cal.append(0)
      
   ventana.destroy()
def test_python(user,contra):
   global perfil
   global cal
   cal=[]
   
   global ventana
   ventana= Tk()
   ventana.geometry=("600x500")
   ventana.title("Test de python")
   ventana.config(bg="yellow")
   ventana.attributes("-topmost", True)
   messagebox.showinfo('Instrucciones',"Selecciona el orden de los siguientes \n" +
                         "fragmentos de programas")

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
            x=[1,2,3,4]
            x=np.random.permutation(x)
            print(x)
            N11 = ImageTk.PhotoImage(Image.open("1 N1.gif"))
            N12 = ImageTk.PhotoImage(Image.open("2 N1.gif"))
            N13 = ImageTk.PhotoImage(Image.open("3 N1.gif"))
            N14 = ImageTk.PhotoImage(Image.open("4 N1.gif"))
            
            E1=Entry(ventana)
            E1.grid(row=2, column=1)
            E2=Entry(ventana)
            E2.grid(row=2, column=3)
            E3=Entry(ventana)
            E3.grid(row=4, column=1)
            E4=Entry(ventana)
            E4.grid(row=4, column=3)
            
            
            if (x[0]==1):
               Im1= Button(ventana, image=N11)
               Im1.grid(row=1, column=1)
            elif (x[0]==2):
               Im1=Button (ventana, image=N12)
               Im1.grid(row=1, column=1)
            elif (x[0]==3):
               Im1= Button(ventana, image=N13)
               Im1.grid(row=1, column=1)
            elif (x[0]==4):
               Im1= Button(ventana, image=N14)
               Im1.grid(row=1, column=1)
            #############################
            if (x[1]==1):
               Im2= Button(ventana, image=N11)
               Im2.grid(row=1, column=3)
            elif (x[1]==2):
               Im2=Button (ventana, image=N12)
               Im2.grid(row=1, column=3)
            elif (x[1]==3):
               Im2= Button(ventana, image=N13)
               Im2.grid(row=1, column=3)
            elif (x[1]==4):
               Im2= Button(ventana, image=N14)
               Im2.grid(row=1, column=3)
            ################################
            if (x[2]==1):
               Im3= Button(ventana, image=N11)
               Im3.grid(row=3, column=1)
            elif (x[2]==2):
               Im3=Button (ventana, image=N12)
               Im3.grid(row=3, column=1)
            elif (x[2]==3):
               Im3= Button(ventana, image=N13)
               Im3.grid(row=3, column=1)
            elif (x[2]==4):
               Im3= Button(ventana, image=N14)
               Im3.grid(row=3, column=1)
         ###############################
            if (x[3]==1):
               Im4= Button(ventana, image=N11)
               Im4.grid(row=3, column=3)
            elif (x[3]==2):
               Im4=Button (ventana, image=N12)
               Im4.grid(row=3, column=3)
            elif (x[3]==3):
               Im4= Button(ventana, image=N13)
               Im4.grid(row=3, column=3)
            elif (x[3]==4):
               Im4= Button(ventana, image=N14)
               Im4.grid(row=3, column=3)
            B_val=Button(ventana,text="Aceptar",command=Validar)
            B_val.grid(row=5,column=2)
            

         elif (Nivel==2):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            
            x=[1,2,3,4]
            x=np.random.permutation(x)
            print(x)
            N21 = ImageTk.PhotoImage(Image.open("1 N2.gif"))
            N22 = ImageTk.PhotoImage(Image.open("2 N2.gif"))
            N23 = ImageTk.PhotoImage(Image.open("3 N2.gif"))
            N24 = ImageTk.PhotoImage(Image.open("4 N2.gif"))
            
            E1=Entry(ventana)
            E1.grid(row=2, column=1)
            E2=Entry(ventana)
            E2.grid(row=2, column=3)
            E3=Entry(ventana)
            E3.grid(row=4, column=1)
            E4=Entry(ventana)
            E4.grid(row=4, column=3)
            
            if (x[0]==1):
               Im1= Button(ventana, image=N21)
               Im1.grid(row=1, column=1)
            elif (x[0]==2):
               Im1=Button (ventana, image=N22)
               Im1.grid(row=1, column=1)
            elif (x[0]==3):
               Im1= Button(ventana, image=N23)
               Im1.grid(row=1, column=1)
            elif (x[0]==4):
               Im1= Button(ventana, image=N24)
               Im1.grid(row=1, column=1)
            #############################
            if (x[1]==1):
               Im2= Button(ventana, image=N21)
               Im2.grid(row=1, column=3)
            elif (x[1]==2):
               Im2=Button (ventana, image=N22)
               Im2.grid(row=1, column=3)
            elif (x[1]==3):
               Im2= Button(ventana, image=N23)
               Im2.grid(row=1, column=3)
            elif (x[1]==4):
               Im2= Button(ventana, image=N24)
               Im2.grid(row=1, column=3)
            ################################
            if (x[2]==1):
               Im3= Button(ventana, image=N21)
               Im3.grid(row=3, column=1)
            elif (x[2]==2):
               Im3=Button (ventana, image=N22)
               Im3.grid(row=3, column=1)
            elif (x[2]==3):
               Im3= Button(ventana, image=N23)
               Im3.grid(row=3, column=1)
            elif (x[2]==4):
               Im3= Button(ventana, image=N24)
               Im3.grid(row=3, column=1)
         ###############################
            if (x[3]==1):
               Im4= Button(ventana, image=N21)
               Im4.grid(row=3, column=3)
            elif (x[3]==2):
               Im4=Button (ventana, image=N22)
               Im4.grid(row=3, column=3)
            elif (x[3]==3):
               Im4= Button(ventana, image=N23)
               Im4.grid(row=3, column=3)
            elif (x[3]==4):
               Im4= Button(ventana, image=N24)
               Im4.grid(row=3, column=3)
            B_val=Button(ventana,text="Aceptar",command=Validar2)
            B_val.grid(row=5,column=2)
            
            pass
         
         elif (Nivel==3):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            
            N31 = ImageTk.PhotoImage(Image.open("FuncionAND.gif"))
            N32 = ImageTk.PhotoImage(Image.open("FuncionOR.gif"))
            N33 = ImageTk.PhotoImage(Image.open("FuncionNOT.gif"))
            
            
            E1=Entry(ventana)
            E1.grid(row=1, column=1)
            E2=Entry(ventana)
            E2.grid(row=3, column=1)
            E3=Entry(ventana)
            E3.grid(row=4, column=1)
            E4=Entry(ventana)
            E4.grid(row=6, column=1)
            E5=Entry(ventana)
            E5.grid(row=7, column=1)
            
            
            Im1= Button(ventana, image=N31)
            Im1.grid(row=2, column=3)

            Im2= Button(ventana, image=N32)
            Im2.grid(row=5, column=3)

            Im3= Button(ventana, image=N33)
            Im3.grid(row=7, column=3)
            
            B_val=Button(ventana,text="Aceptar",command=Validar3)
            B_val.grid(row=8, column=2)
            
            pass
         
         elif (Nivel==4):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            
            N41 = ImageTk.PhotoImage(Image.open("BooleAND.gif"))
            N42 = ImageTk.PhotoImage(Image.open("BooleOR.gif"))
            N43 = ImageTk.PhotoImage(Image.open("BooleConv.gif"))
            
            
            E1=Entry(ventana)
            E1.grid(row=2, column=1)
            E2=Entry(ventana)
            E2.grid(row=2, column=2)
            E3=Entry(ventana)
            E3.grid(row=2, column=3)
            
        
            
            Im1= Button(ventana, image=N41)
            Im1.grid(row=1, column=1)

            Im2= Button(ventana, image=N42)
            Im2.grid(row=1, column=2)

            Im3= Button(ventana, image=N43)
            Im3.grid(row=1, column=3)
            
            B_val=Button(ventana,text="Aceptar",command=Validar4)
            B_val.grid(row=3, column=2)
            
            pass
         
         elif (Nivel==5):
            ventana= Tk()
            ventana.geometry=("600x500")
            ventana.title("Test de pruebas python")
            ventana.config(bg="yellow")
            
            N51 = ImageTk.PhotoImage(Image.open("FuncionIF.gif"))
            N52 = ImageTk.PhotoImage(Image.open("FuncionELIF.gif"))
            N53 = ImageTk.PhotoImage(Image.open("FuncionIFAN.gif"))
            vector=[" ","Correcto","Incorrecto"]
            
            E1=Spinbox(ventana, values=vector)
            E1.grid(row=2, column=1)
            E2=Spinbox(ventana, values=vector)
            E2.grid(row=2, column=2)
            E3=Spinbox(ventana, values=vector)
            E3.grid(row=4, column=1)
            
            Im1= Button(ventana, image=N51)
            Im1.grid(row=1, column=1)

            Im2= Button(ventana, image=N52)
            Im2.grid(row=1, column=2)

            Im3= Button(ventana, image=N53)
            Im3.grid(row=3, column=1)
            
            B_val=Button(ventana,text="Aceptar",command=Validar5)
            B_val.grid(row=3, column=2)
            
            pass
         elif (Nivel==6):
            final(user,contra)
            pass
         elif (Nivel==7):
            pass
         elif (Nivel==8):
            pass
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
      #except:
      #   print("error")
