import sys
import pygame
import os
WIDTH = 623
HEIGHT = 150
pygame.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )

class BG:
    def __init__(self,x):
        #Funcion BG. define la posicion X y la textura del fondo antes de mostrarlo
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = 0
        self.set_texture()
        self.show()

    def update(self, dx):
        #Funcion Update. En caso de que el fondo de pantalla llegue a su limite X, reinicia la posicion
        self.x += dx
        if self.x <= -WIDTH:
            self.x = WIDTH    

    def show(self):
        #Funcion Show. Hace que se muestre la textura
        screen.blit(self.texture, (self.x,self.y))

    def set_texture(self):
        #Funcion Set_Texture. Establece el path para la textura y la acomoda al tamaño de la ventana
        path = os.path.join('assets/images/bg.png')
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture,(self.width,self.height))

class Game:
    #Clase Game. Se ejecuta la clase Background y se establecen las posiciones y la velocidad
    def __init__(self):
        self.bg = [BG(x=0),BG(x=WIDTH)]
        self.speed = 3

def main():
    #Funcion principal.  aqui se ejecuta toda la magia :3
    #se hace un print inicial... no preguntes porque
    print("hewwo!")
    #se crea un nuevo objeto Game
    game = Game()
    #se establece un clock para evitar velocidad excesiva. ***DO NOT DELETE***
    clock = pygame.time.Clock()
    #main loop. la parte donde todo se 
    while True:
        try:
            for bg in game.bg:
                bg.update(-game.speed)
                bg.show()
        except:
            pygame.quit()
            sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("adius :3")
                pygame.quit()
                sys.exit()
        
        clock.tick(80)
        pygame.display.update()

main()

