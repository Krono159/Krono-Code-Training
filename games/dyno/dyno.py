import os
import sys
import math
import random
import pygame
prevrand = 0
WIDTH = 623
HEIGHT = 150

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption('DinOwO')

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

class Dino:
    def __init__(self):
        self.width = 44
        self.height = 44
        self.x = 10
        self.y = 80
        self.sprite = 0
        self.dy = 3
        self.gravity = 1.2
        self.onground = True
        self.jumping = False
        self.jumpstop = 10
        self.falling = False
        self.fallstop = 80
        self.set_texture()
        self.show
    
    def update(self,loop):
        #jumping
        if self.jumping:
            self.y -= self.dy
            if self.y <= self.jumpstop:
                self.fall()
        #falling
        elif self.falling:
            self.y += self.gravity * self.dy
            if self.y >= self.fallstop:
                self.stop()
        elif self.onground and loop % 4 == 0:
            self.sprite = (self.sprite+1) % 3
            self.set_texture()
        
        #waling
            
    def show(self):
        #Funcion Show. Hace que se muestre la textura
        screen.blit(self.texture, (self.x,self.y))

    def set_texture(self):
        #Funcion Set_Texture. Establece el path para la textura y la acomoda al tamaño de la ventana
        path = os.path.join(f'assets/images/dino{self.sprite}.png')
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture,(self.width,self.height))

    def jump(self):
        self.jumping = True
        self.onground = False
    
    def fall(self):
        self.jumping = False
        self.falling = True
    
    def stop(self):
        self.falling = False
        self.onground = True

class Cactus:
    def __init__(self,x):
        self.width = 34
        self.height = 44
        self.x = x
        self.y = 80
        self.set_texture()
        self.show()

    def update(self,dx):
        self.x += dx
        if self.x <= -WIDTH:
            self.x = WIDTH    

    def show(self):
        screen.blit(self.texture, (self.x,self.y))

    def set_texture(self):
        path = os.path.join('assets/images/cactus.png')
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture,(self.width,self.height))
        
class Game:
    #Clase Game. Se ejecuta la clase Background y se establecen las posiciones y la velocidad
    def __init__(self):
        self.bg = [BG(x=0),BG(x=WIDTH)]
        self.dino = Dino()
        self.obstacles = []
        self.speed = 3
        self.prevrand = 0
        self.anotherrand = 0
        self.spawncactus()

    def tospawn(self,loops ):
        print(loops % 100 == 0)
        return loops % 100 == 0
        

        pass

    def spawncactus(self):
        if len(self.obstacles) > 0 and len(self.obstacles):
            prev_cactus = self.obstacles[-1]
            x = random.randint(prev_cactus.x + self.dino.width + 84, WIDTH + prev_cactus.x + self.dino.width + 84 )
            print("X = ",x)
            #if prev_cactus.x in range (x - 44, x + 45):
            #    pass
            #else:
             #   new_cactus = Cactus(x)
        #emptylist
        else:
            x = random.randint(WIDTH + 44, 1000)
        cactus = Cactus(x)
        self.obstacles.append(cactus)
        #crea un nuevo cactus
def main():
    #Funcion principal.  aqui se ejecuta toda la magia :3
    #se hace un print inicial... no preguntes porque
    print("hewwo!")
    speed = 80
    looped = 0
    #objetos
    game = Game()
    dinosaurio = game.dino

    #se establece un clock para evitar velocidad excesiva. ***DO NOT DELETE***
    clock = pygame.time.Clock()

    loop = 0
    #main loop. la parte donde todo se 
    while True:
        
        #var overflow protection

        loop += 1
        if loop >= 15000:
            loop = 0
        #----------------bg-------------------
        
        for bg in game.bg:
            bg.update(-game.speed)
            bg.show()
        #-----------------dino-------------------
        dinosaurio.update(loop)
        dinosaurio.show()


        #-----------------cactus-------------------

        if game.tospawn(loop):
                game.spawncactus()

        for cactus in game.obstacles:
            cactus.update(-game.speed)
            cactus.show()



        #-------------------EVENTOS------------------

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if dinosaurio.onground == True:
                        dinosaurio.jump()
                if event.key == pygame.K_RSHIFT:
                    print(game.obstacles)

            if event.type == pygame.QUIT:
                print("adius :3")
                pygame.quit()
                sys.exit()

        clock.tick(80)
        pygame.display.update()

main()

