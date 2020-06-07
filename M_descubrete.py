from tkinter import *
from tkinter import messagebox
global Concentracion
global Creatividad
global Expresion
global SP1
global SP2
global SP3
global SP4
global SP5
global SP6
global SP7
global SP8
global SP9
global SP10
global SP11
global SP12
global usuario
global cont
def Funcion():
   import sqlite3
   global usuario
   global cont
   global Concentracion
   global Creatividad
   global Expresion
   global SP1
   global SP2
   global SP3
   global SP4
   global SP5
   global SP6
   global SP7
   global SP8
   global SP9
   global SP10
   global SP11
   global SP12
   
   
   vector=["Nada","Poco","Mucho"]
   if (str(SP1.get())==vector[0]):
      Concentracion=Concentracion+0
   elif (str(SP1.get())==vector[1]):
      Concentracion=Concentracion+1
   elif (str(SP1.get())==vector[2]):
      Concentracion=Concentracion+2
      
   if (str(SP7.get())==vector[0]):
      Concentracion=Concentracion+0
   elif (str(SP7.get())==vector[1]):
      Concentracion=Concentracion+1
   elif (str(SP7.get())==vector[2]):
      Concentracion=Concentracion+2

   if (str(SP9.get())==vector[0]):
      Concentracion=Concentracion+0
   elif (str(SP9.get())==vector[1]):
      Concentracion=Concentracion+1
   elif (str(SP9.get())==vector[2]):
      Concentracion=Concentracion+2

   if (str(SP11.get())==vector[0]):
      Concentracion=Concentracion+0
   elif (str(SP11.get())==vector[1]):
      Concentracion=Concentracion+1
   elif (str(SP11.get())==vector[2]):
      Concentracion=Concentracion+2
   
   if (str(SP2.get())==vector[0]):
      Expresion=Expresion+0
   elif (str(SP2.get())==vector[1]):
      Expresion=Expresion+1
   elif (str(SP2.get())==vector[2]):
      Expresion=Expresion+2

   if (str(SP4.get())==vector[0]):
      Expresion=Expresion+0
   elif (str(SP4.get())==vector[1]):
      Expresion=Expresion+1
   elif (str(SP4.get())==vector[2]):
      Expresion=Expresion+2

   if (str(SP6.get())==vector[0]):
      Expresion=Expresion+0
   elif (str(SP6.get())==vector[1]):
      Expresion=Expresion+1
   elif (str(SP6.get())==vector[2]):
      Expresion=Expresion+2

   if (str(SP8.get())==vector[0]):
      Expresion=Expresion+0
   elif (str(SP8.get())==vector[1]):
      Expresion=Expresion+1
   elif (str(SP8.get())==vector[2]):
      Expresion=Expresion+2

   if (str(SP3.get())==vector[0]):
      Creatividad=Creatividad+0
   if (str(SP3.get())==vector[1]):
      Creatividad=Creatividad+1
   if (str(SP3.get())==vector[2]):
      Creatividad=Creatividad+2

   if (str(SP5.get())==vector[0]):
      Creatividad=Creatividad+0
   if (str(SP5.get())==vector[1]):
      Creatividad=Creatividad+1
   if (str(SP5.get())==vector[2]):
      Creatividad=Creatividad+2

   if (str(SP10.get())==vector[0]):
      Creatividad=Creatividad+0
   if (str(SP10.get())==vector[1]):
      Creatividad=Creatividad+1
   if (str(SP10.get())==vector[2]):
      Creatividad=Creatividad+2

   if (str(SP12.get())==vector[0]):
      Creatividad=Creatividad+0
   if (str(SP12.get())==vector[1]):
      Creatividad=Creatividad+1
   if (str(SP12.get())==vector[2]):
      Creatividad=Creatividad+2

   #print(Creatividad)
   #print(Expresion)
   #print(Concentracion)
   con = sqlite3.connect('datos.db')
   cur = con.cursor()
   cur.execute('SELECT * FROM usuarios WHERE correo = ? AND contraseña = ? ',(usuario,cont))
   perfil = cur.fetchone()
   sql = ("UPDATE usuarios SET creatividad='"+str(Creatividad)+"',expresion='"+str(Expresion)+
          "',concentracion='"+str(Concentracion)+"' WHERE correo='"+usuario+"'")
   #print(sql)
   cur.execute(sql)
   con.commit()
   con.close()
   ventana.destroy()
   exit()

   Creatividad=0
   Expresion=0
   Concentracion=0

def test_descubrete(user,contra):
   global usuario
   global cont
   usuario=user
   cont=contra
   print(usuario)
   print(cont)
   global SP1
   global SP2
   global SP3
   global SP4
   global SP5
   global SP6
   global SP7
   global SP8
   global SP9
   global SP10
   global SP11
   global SP12
   global Concentracion
   global Creatividad
   global Expresion
   Concentracion=0
   Creatividad=0
   Expresion=0
   
   global ventana
   ventana= Tk()
   ventana.geometry=("1000x800")
   ventana.title("Test descubrete")
   ventana.config(bg="yellow")
   ventana.attributes("-topmost", True)
   vector=["Nada","Poco","Mucho"]

   P1=Label(ventana,text="Logro completar las tareas con éxito")
   P2=Label(ventana,text="Me gusta hablar en público")
   P3=Label(ventana,text="Me gusta el arte (pintura, manualidades, música)")
   P4=Label(ventana,text="Me gustaria ser expositor o conferensista")
   P5=Label(ventana,text="Me considero una paciente y creativa")
   P6=Label(ventana,text="Soy el alma de la fiesta en las reuniones con amigos")
   P7=Label(ventana,text="Veo a la gente a los ojos cuando platico con otra persona")
   P8=Label(ventana,text="Me gusta ser lider y dar ordenes en mis actividades en equipo")
   P9=Label(ventana,text="Me gusta seguir instrucciones")
   P10=Label(ventana,text="Cuando leo un libro, me imagino lo que leo")
   P11=Label(ventana,text="En un exámen me logro concentrar sin dejar preguntas en blanco")
   P12=Label(ventana,text="Al ver una pelicula, me imagino dentro de la pelicula")
   
   Pr1=Label(ventana,text="")
   Pr2=Label(ventana,text="")
   Pr3=Label(ventana,text="")
   Pr4=Label(ventana,text="")
   Pr5=Label(ventana,text="")
   Pr6=Label(ventana,text="")
   Pr7=Label(ventana,text="")
   Pr8=Label(ventana,text="")
   Pr9=Label(ventana,text="")
   Pr10=Label(ventana,text="")
   Pr11=Label(ventana,text="")
   Pr12=Label(ventana,text="")
   SP1=Spinbox(ventana,values=vector)
   SP2=Spinbox(ventana,values=vector)
   SP3=Spinbox(ventana,values=vector)
   SP4=Spinbox(ventana,values=vector)
   SP5=Spinbox(ventana,values=vector)
   SP6=Spinbox(ventana,values=vector)
   SP7=Spinbox(ventana,values=vector)
   SP8=Spinbox(ventana,values=vector)
   SP9=Spinbox(ventana,values=vector)
   SP10=Spinbox(ventana,values=vector)
   SP11=Spinbox(ventana,values=vector)
   SP12=Spinbox(ventana,values=vector)
   P1.grid(row=1,column=1)
   SP1.grid(row=1,column=3)
   P2.grid(row=3,column=1)
   SP2.grid(row=3,column=3)
   P3.grid(row=5,column=1)
   SP3.grid(row=5,column=3)
   P4.grid(row=7,column=1)
   SP4.grid(row=7,column=3)
   P5.grid(row=9,column=1)
   SP5.grid(row=9,column=3)
   P6.grid(row=11,column=1)
   SP6.grid(row=11,column=3)
   P7.grid(row=13,column=1)
   SP7.grid(row=13,column=3)
   P8.grid(row=15,column=1)
   SP8.grid(row=15,column=3)
   P9.grid(row=17,column=1)
   SP9.grid(row=17,column=3)
   P10.grid(row=19,column=1)
   SP10.grid(row=19,column=3)
   P11.grid(row=21,column=1)
   SP11.grid(row=21,column=3)
   P12.grid(row=23,column=1)
   SP12.grid(row=23,column=3)
   Pr1.grid(row=2,column=1)
   Pr2.grid(row=4,column=1)
   Pr3.grid(row=6,column=1)
   Pr4.grid(row=8,column=1)
   Pr5.grid(row=10,column=1)
   Pr6.grid(row=12,column=1)
   Pr7.grid(row=14,column=1)
   Pr8.grid(row=16,column=1)
   Pr9.grid(row=18,column=1)
   Pr10.grid(row=20,column=1)
   Pr11.grid(row=22,column=1)
   Pr12.grid(row=24,column=1)

   Btn=Button(ventana, text="Descubrirme",command=Funcion)
   Btn.grid(row=25, column=2)
   ventana.mainloop()
   
