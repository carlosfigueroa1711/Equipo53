#Juego de conocimiento de lenguajes de programacion
#Juego basado en tetris

from tkinter import *
from tkinter import messagebox
global ventana

def F_python():
   global ventana
   import M_Python
   #ventana.destroy()
   M_Python.test_python()
def F_Java():
   print("Java test")
def F_C():
   global ventana
   import M_C
   #ventana.destroy()
   M_C.test_C()
   
   print("C test")

def F_R():
   global ventana
   import M_R
   #ventana.destroy()
   M_R.test_R()
   print("R test")
   
def Descubrete():
   global ventana
   import M_descubrete
   messagebox.showinfo('Instrucciones',"Selecciona la opción que mas te identifiques. \n"+
                       "Describete tal como eres en la actualidad, no como desearias ser")
   
   M_descubrete.test_descubrete()
  
   #print("Test descubrete")

def menu():
   global ventana
   ventana=Tk()
   ventana.geometry('400x300')
   ventana.title("Elige un lenguaje")
   ventana.config(bg="blue")
   ventana.update()

   Py=Button(ventana,text="Python",width=20, height=5,command=F_python)
   Py.place(x=5, y=5)

   Jb=Button(ventana,text="Java",width=20, height=5,command=F_Java)
   Jb.place(x=200, y=5)

   C=Button(ventana,text="C",width=20, height=5,command=F_C)
   C.place(x=5, y=100)

   R=Button(ventana,text="R",width=20, height=5,command=F_R)
   R.place(x=200, y=100)

   Des=Button(ventana,text="Descubrete",width=20, height=5,command=Descubrete,bg='pink')
   Des.place(x=100, y=200)


   ventana.mainloop()
