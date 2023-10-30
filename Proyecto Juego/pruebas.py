import pygame
from Constantes import *

#inicia pygame
pygame.init()

#Tamaño de la ventana y nombre
ventana = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
pygame.display.set_caption("Pygame")

#Evento de tiempo
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,10)

#inicializo variables
posicion_click = [100,100]

#cargo la imagen
imagen_background = pygame.image.load("Background.png")
running = True
while running:
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        #captura el evento click del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            #me guarda en una variable las "coordenadas" del click en pixeles
            posicion_click = list(event.pos)
        if event.type == timer_segundos:
            if posicion_click[0] < ANCHO_VENTANA + 80:
                posicion_click[0] += 1
            else:
                posicion_click[0] = -80
        if event.type == pygame.KEYDOWN:
            pass
    #Le doy un color al fondo
    ventana.fill(COLOR_AZUL)
    
    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_LEFT] :
        posicion_click[1] = posicion_click[1] + 1
    #crear un circulo
    pygame.draw.circle(ventana,COLOR_NEGRO,posicion_click,80)
    ventana.blit(imagen_background,(0,0,50,50))
    #actualiza la pantalla
    pygame.display.flip()

#cierra pygame
pygame.quit()