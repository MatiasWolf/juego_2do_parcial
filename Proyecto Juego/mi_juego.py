import pygame
from Constantes import *

#inicia pygame
pygame.init()

#Tamaño de la ventana y nombre
ventana = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
pygame.display.set_caption("Pygame")

x = 0
#Inicializo el manejo de los frames por segundo del fondo
FPS_fondo = 200
FPS_personaje = 15
RELOJ_FONDO = pygame.time.Clock()
RELOJ_PERSONAJE = pygame.time.Clock()

#cargo la imagen
imagen_background = pygame.image.load("Background.png").convert()

#Personaje
correr_derecha = [pygame.image.load("sprites_correr/correr_d_01.png"),
    pygame.image.load("sprites_correr/correr_d_02.png"),
    pygame.image.load("sprites_correr/correr_d_03.png"),
    pygame.image.load("sprites_correr/correr_d_04.png"),
    pygame.image.load("sprites_correr/correr_d_05.png"),
    pygame.image.load("sprites_correr/correr_d_06.png"),
    pygame.image.load("sprites_correr/correr_d_07.png"),
    pygame.image.load("sprites_correr/correr_d_08.png"),
    pygame.image.load("sprites_correr/correr_d_09.png"),
    pygame.image.load("sprites_correr/correr_d_10.png")]

quieto = [pygame.image.load("sprites_quieto/quieto_d_01.png"),
    pygame.image.load("sprites_quieto/quieto_d_02.png"),
    pygame.image.load("sprites_quieto/quieto_d_03.png"),
    pygame.image.load("sprites_quieto/quieto_d_04.png"),
    pygame.image.load("sprites_quieto/quieto_d_05.png"),
    pygame.image.load("sprites_quieto/quieto_d_06.png"),
    pygame.image.load("sprites_quieto/quieto_d_07.png"),
    pygame.image.load("sprites_quieto/quieto_d_08.png"),
    pygame.image.load("sprites_quieto/quieto_d_09.png"),
    pygame.image.load("sprites_quieto/quieto_d_10.png"),]

#Coordenadas del personaje inicial
px = 50
py = 700
velocidad = 10

#Variables de movimiento
salto = False
cuenta_salto = 10

izq = False
der = False

cuenta_pasos = 0

def mover_personaje():
    global cuenta_pasos
    global x
    
    if cuenta_pasos + 1 >= 10:
        cuenta_pasos = 0
    
    if izq:
        pass
    elif der:
        ventana.blit(correr_derecha[cuenta_pasos // 1], (int(px),int(py)))
        cuenta_pasos += 1
    elif salto:
        pass
    else:
        ventana.blit(quieto[cuenta_pasos // 1], (int(px),int(py)))
        cuenta_pasos += 1

posicion_click = [100,100]
running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        #captura el evento click del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            #me guarda en una variable las "coordenadas" del click en pixeles
            posicion_click = list(event.pos)
        lista_teclas = pygame.key.get_pressed()
    
    mover_derecha = lista_teclas[pygame.K_d]
    if mover_derecha:
        px += velocidad
        izq = False
        der = True
    else:
        izq = False
        der = False
    
    
    
    #Darle movimiento al fondo (falta crear el personaje y que el fondo se mueva conforme avanza o retrocede el pj)
    x_relativa = x % imagen_background.get_rect().width
    ventana.blit(imagen_background,(x_relativa - imagen_background.get_rect().width,0))
    if x_relativa < ANCHO_VENTANA:
        ventana.blit(imagen_background,(x_relativa,0))
    
    x -= 1
    mover_personaje()
    #actualiza la pantalla
    pygame.display.flip()
    #Controla los fps del fondo
    RELOJ_PERSONAJE.tick(FPS_personaje)
    RELOJ_FONDO.tick(FPS_fondo)
    

#cierra pygame
pygame.quit()