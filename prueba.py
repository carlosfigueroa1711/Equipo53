import pygame, sys
from pygame.locals import *

pygame.init()

global DISPLAYSURF
global fondo1
global fondo2
global fondo3
global fondo4
global fpsClock
global FPS
global bandera
global F
global Nivel
global posicion
global player
global monedas

DISPLAYSURF = pygame.display.set_mode((807, 674))
pygame.display.set_caption('Hello World!') #Titulo de la pantalla

def Nivel1():
   global monedas
   pantalla=1
   correcta=0
   incorrecta=0
   BLUE=(0,0,255)
   WHITE=(255,255,255)
   pygame.mixer.music.stop()
   HP_Player=200
   HP_Enemigo=200
   c=0
   while True:
      while (pantalla==1):
         fondo = pygame.image.load("Enemigo Nivel 1.png")
         DISPLAYSURF.blit(fondo,(0,0))
   #   if (correcta==0 and incorrecta==0): 
         pygame.draw.rect(DISPLAYSURF,WHITE,(42, 44, 442, 274))
         pygame.draw.rect(DISPLAYSURF,WHITE,(300, 368, 442, 274))
         pygame.draw.line(DISPLAYSURF, BLUE, (30, 368), ((30+HP_Player), 368), 20)
         pygame.draw.line(DISPLAYSURF, BLUE, (582, 276), ((582+HP_Enemigo), 276), 20)
         Pregunta=pygame.image.load("Pregunta_1.png")
         DISPLAYSURF.blit(Pregunta,(44,50))
         R_e1=pygame.image.load("if1a.png")
         DISPLAYSURF.blit(R_e1,(300,368))
         R_e2=pygame.image.load("if1b.png")
         DISPLAYSURF.blit(R_e1,(521,368))
         R_e3=pygame.image.load("if1c.png")
         DISPLAYSURF.blit(R_e1,(300,512))
         R_C=pygame.image.load("if1cor.png")
         DISPLAYSURF.blit(R_e1,(521,512))

         F_arriba=pygame.image.load("flecha_arriba.png")
         DISPLAYSURF.blit(F_arriba,(370,440))
         F_abajo=pygame.image.load("flecha_abajo.png")
         DISPLAYSURF.blit(F_abajo,(591,440))
         F_izquierda=pygame.image.load("flecha_izquierda.png")
         DISPLAYSURF.blit(F_izquierda,(370,590))
         F_derecha=pygame.image.load("flecha_derecha.png")
         DISPLAYSURF.blit(F_derecha,(591,590))
            
         pygame.display.update()
         fpsClock.tick(FPS)
         for event in pygame.event.get():
            if(event.type==KEYDOWN):
               if (event.key==K_UP):
                  correcta=1
                  HP_Player=HP_Player
                  HP_Enemigo=HP_Enemigo-67
               if (event.key==K_DOWN):
                  incorrecta=incorrecta+1
                  HP_Player=HP_Player-67
                  HP_Enemigo=HP_Enemigo
               if (event.key==K_LEFT):
                  incorrecta=incorrecta+1
                  HP_Player=HP_Player-67
                  HP_Enemigo=HP_Enemigo
               if (event.key==K_RIGHT):
                  incorrecta=incorrecta+1
                  HP_Player=HP_Player-67
                  HP_Enemigo=HP_Enemigo
               ##Nivel 2
               if (event.key==K_BACKSPACE):
                  principal()
            if event.type==QUIT:
               pygame.quit()
               sys.exit()
      





def carga(Nivel):
   global player
   global fondo1
   global fondo2
   global fondo3
   global fondo4
   if (Nivel==1):
      fondo1 = pygame.image.load("Titulo_1.png") #Imagen de fondo
      fondo2 = pygame.image.load("Titulo_1_1.png") #Imagen de fondo
      fondo3 = pygame.image.load("Titulo_1_2.png") #Imagen de fondo
      fondo4 = pygame.image.load("Titulo_1_3.png") #Imagen de fondo

   elif (Nivel==2):
      fondo1 = pygame.image.load("Titulo_2.png") #Imagen de fondo
      fondo2 = pygame.image.load("Titulo_2_1.png") #Imagen de fondo
      fondo3 = pygame.image.load("Titulo_2_2.png") #Imagen de fondo
      fondo4 = pygame.image.load("Titulo_2_3.png") #Imagen de fondo

   elif (Nivel==3):
      fondo1 = pygame.image.load("Titulo_3.png") #Imagen de fondo
      fondo2 = pygame.image.load("Titulo_3_1.png") #Imagen de fondo
      fondo3 = pygame.image.load("Titulo_3_2.png") #Imagen de fondo
      fondo4 = pygame.image.load("Titulo_3_3.png") #Imagen de fondo
      
   elif (Nivel==4):
      fondo1 = pygame.image.load("Titulo_4.png") #Imagen de fondo
      fondo2 = pygame.image.load("Titulo_4_1.png") #Imagen de fondo
      fondo3 = pygame.image.load("Titulo_4_2.png") #Imagen de fondo
      fondo4 = pygame.image.load("Titulo_4_3.png") #Imagen de fondo
      
   elif (Nivel==5):
      fondo1 = pygame.image.load("Titulo_5.png") #Imagen de fondo
      fondo2 = pygame.image.load("Titulo_5_1.png") #Imagen de fondo
      fondo3 = pygame.image.load("Titulo_5_2.png") #Imagen de fondo
      fondo4 = pygame.image.load("Titulo_5_3.png") #Imagen de fondo
      
   elif (Nivel==6):
      fondo1 = pygame.image.load("Titulo_6.png") #Imagen de fondo
      fondo2 = pygame.image.load("Titulo_6_1.png") #Imagen de fondo
      fondo3 = pygame.image.load("Titulo_6_2.png") #Imagen de fondo
      fondo4 = pygame.image.load("Titulo_6_3.png") #Imagen de fondo
      

def principal():
   global fpsClock
   global FPS
   global Nivel
   global bandera
   pygame.mixer.music.load("Titulo.mp3")
   pygame.mixer.music.play()
   c=0
   fpsClock = pygame.time.Clock()
   FPS=60
   F=0
   bandera=0
   Nivel=6
   Posicion=1
   player = pygame.image.load("Player_m.png") 
   while True: # main game loop
      c=c+1
      if(c==510):
         c=0
         pygame.mixer.music.stop()
         #pygame.mixer.music.play()
         
      if (bandera==0):
         carga(Nivel)
         bandera=1
      if(F<=2):
         DISPLAYSURF.blit(fondo1,(0,0))
         if (Posicion==1):
            DISPLAYSURF.blit(player,(459,434))
         elif (Posicion==2):
            DISPLAYSURF.blit(player,(448,280))
         elif (Posicion==3):
            DISPLAYSURF.blit(player,(545,179))
         elif (Posicion==4):
            DISPLAYSURF.blit(player,(215,326))
         elif (Posicion==5):
            DISPLAYSURF.blit(player,(231,491))
         elif (Posicion==6):
            DISPLAYSURF.blit(player,(570,50))
                     
            
      elif((F>2) and F<=4):
         DISPLAYSURF.blit(fondo2,(0,0))
         if (Posicion==1):
            DISPLAYSURF.blit(player,(459,434))
         elif (Posicion==2):
            DISPLAYSURF.blit(player,(448,280))
         elif (Posicion==3):
            DISPLAYSURF.blit(player,(545,179))
         elif (Posicion==4):
            DISPLAYSURF.blit(player,(215,326))
         elif (Posicion==5):
            DISPLAYSURF.blit(player,(231,491))
         elif (Posicion==6):
            DISPLAYSURF.blit(player,(570,50))
            
      elif((F>4) and F<=6):
         DISPLAYSURF.blit(fondo3,(0,0))
         if (Posicion==1):
            DISPLAYSURF.blit(player,(459,434))
         elif (Posicion==2):
            DISPLAYSURF.blit(player,(448,280))
         elif (Posicion==3):
            DISPLAYSURF.blit(player,(545,179))
         elif (Posicion==4):
            DISPLAYSURF.blit(player,(215,326))
         elif (Posicion==5):
            DISPLAYSURF.blit(player,(231,491))
         elif (Posicion==6):
            DISPLAYSURF.blit(player,(570,50))
            
      elif((F>6) and F<=8):
         DISPLAYSURF.blit(fondo4,(0,0))
         if (Posicion==1):
            DISPLAYSURF.blit(player,(459,434))
         elif (Posicion==2):
            DISPLAYSURF.blit(player,(448,280))
         elif (Posicion==3):
            DISPLAYSURF.blit(player,(545,179))
         elif (Posicion==4):
            DISPLAYSURF.blit(player,(215,326))
         elif (Posicion==5):
            DISPLAYSURF.blit(player,(231,491))
         elif (Posicion==6):
            DISPLAYSURF.blit(player,(570,50))
            
      elif((F>8) and F<=10):
         DISPLAYSURF.blit(fondo3,(0,0))
         if (Posicion==1):
            DISPLAYSURF.blit(player,(459,434))
         elif (Posicion==2):
            DISPLAYSURF.blit(player,(448,280))
         elif (Posicion==3):
            DISPLAYSURF.blit(player,(545,179))
         elif (Posicion==4):
            DISPLAYSURF.blit(player,(215,326))
         elif (Posicion==5):
            DISPLAYSURF.blit(player,(231,491))
         elif (Posicion==6):
            DISPLAYSURF.blit(player,(570,50))
            
      elif((F>10) and F<=12):
         DISPLAYSURF.blit(fondo2,(0,0))
         if (Posicion==1):
            DISPLAYSURF.blit(player,(459,434))
         elif (Posicion==2):
            DISPLAYSURF.blit(player,(448,280))
         elif (Posicion==3):
            DISPLAYSURF.blit(player,(545,179))
         elif (Posicion==4):
            DISPLAYSURF.blit(player,(215,326))
         elif (Posicion==5):
            DISPLAYSURF.blit(player,(231,491))
         elif (Posicion==6):
            DISPLAYSURF.blit(player,(570,50))
         F=0
      F=F+1

      #DISPLAYSURF.fill(color="WHITE")
      
      for event in pygame.event.get():
         if(event.type==KEYDOWN):
            ##Nivel 2
            if (Nivel==2 and Posicion==1 and event.key==K_UP):
               Posicion=2
            elif (Nivel==2 and Posicion==2 and event.key==K_DOWN):
               Posicion=1
            if (event.key==K_SPACE and Posicion==1):
               Nivel1()
            ##Nivel 3
            if (Nivel==3 and Posicion==1 and event.key==K_UP):
               Posicion=2
            elif (Nivel==3 and Posicion==2 and event.key==K_UP):
               Posicion=3
            elif (Nivel==3 and Posicion==2 and event.key==K_DOWN):
               Posicion=1
            elif (Nivel==3 and Posicion==3 and event.key==K_DOWN):
               Posicion=2
            ##Nivel 4
            if (Nivel==4 and Posicion==1 and event.key==K_UP):
               Posicion=2
            elif (Nivel==4 and Posicion==2 and event.key==K_UP):
               Posicion=3
            elif (Nivel==4 and Posicion==2 and event.key==K_DOWN):
               Posicion=1
            elif (Nivel==4 and Posicion==3 and event.key==K_LEFT):
               Posicion=4
            elif (Nivel==4 and Posicion==3 and event.key==K_DOWN):
               Posicion=2
            elif (Nivel==4 and Posicion==4 and event.key==K_RIGHT):
               Posicion=3
            ##Nivel 5
            if (Nivel==5 and Posicion==1 and event.key==K_UP):
               Posicion=2
            elif (Nivel==5 and Posicion==2 and event.key==K_UP):
               Posicion=3
            elif (Nivel==5 and Posicion==2 and event.key==K_DOWN):
               Posicion=1
            elif (Nivel==5 and Posicion==3 and event.key==K_LEFT):
               Posicion=4
            elif (Nivel==5 and Posicion==3 and event.key==K_DOWN):
               Posicion=2
            elif (Nivel==5 and Posicion==4 and event.key==K_RIGHT):
               Posicion=3
            elif (Nivel==5 and Posicion==4 and event.key==K_DOWN):
               Posicion=5
            elif (Nivel==5 and Posicion==5 and event.key==K_UP):
               Posicion=4
            ##Nivel 6
            if (Nivel==6 and Posicion==1 and event.key==K_UP):
               Posicion=2
            elif (Nivel==6 and Posicion==2 and event.key==K_UP):
               Posicion=3
            elif (Nivel==6 and Posicion==2 and event.key==K_DOWN):
               Posicion=1
            elif (Nivel==6 and Posicion==3 and event.key==K_LEFT):
               Posicion=4
            elif (Nivel==6 and Posicion==3 and event.key==K_DOWN):
               Posicion=2
            elif (Nivel==6 and Posicion==4 and event.key==K_RIGHT):
               Posicion=3
            elif (Nivel==6 and Posicion==4 and event.key==K_DOWN):
               Posicion=5
            elif (Nivel==6 and Posicion==5 and event.key==K_UP):
               Posicion=4
            elif (Nivel==6 and Posicion==5 and event.key==K_LEFT):
               Posicion=6
            elif (Nivel==6 and Posicion==6 and event.key==K_RIGHT):
               Posicion=5
                             
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
      pygame.display.update()
      fpsClock.tick(FPS)

principal()
