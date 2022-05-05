import pygame
import random
import math
pygame.init()  
pygame.display.set_caption("Eel")  
screen = pygame.display.set_mode((1000,1000))  
screen.fill((0,0,0))
red = (255,0,0)

#Eel = pygame.image.load('eelface.png') #load your spritesheet
#Eel.set_colorkey((255,0,255)) #this makes bright pink (255, 0, 255) transparent (sort of)
fishy = pygame.image.load('fishy.png')
fishy.set_colorkey((255,255,255))
clock = pygame.time.Clock()
gameover = False

def CircleCollision(x1,x2,y1,y2, radius):
    if (math.sqrt((x2 - x1)**2 + (y2- y1)**2))<radius:
        return True
    else:
        return False

#set up first circle's position and color and size
num = random.randrange(1, 800)
num1 = random.randrange(1, 800)
c1 = random.randrange(1, 255)
c2 = random.randrange(1, 255)
c3 = random.randrange(1, 255)
s = random.randrange(10, 100)
#set up variable to hold mouse position
xpos=0
ypos=0
mousePos = (xpos, ypos)


while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS

#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()    


#Input Section------------------------------------------------------------

    if event.type == pygame.MOUSEBUTTONDOWN:#CLICK
        mousePos = event.pos

    if event.type == pygame.MOUSEBUTTONUP:#release
        draw = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
       
    if event.type == pygame.QUIT: #close game window
        break        
 
    #physics/movement section-----------------------------------------
   
    #try to call the function here, use the new variables
    #(put the call inside an if statement, and only get new points for the circle when it's clicked on)
    if CircleCollision(num,mousePos[0], mousePos[1],num1, s)==True:
        num = random.randrange(1, 800)
        num1 = random.randrange(1, 800)
        c1 = random.randrange(1, 255)
        c2 = random.randrange(1, 255)
        c3 = random.randrange(1, 255)
        s = random.randrange(10, 21)
   
    #Render Section ---------------------------
    screen.fill((0,0,255))
    screen.blit(fishy,(num, num1,25,25))
    pygame.draw.rect(screen, (red), (200,200,25,25))
    #screen.blit(Eel, (Px, Py), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))    


    pygame.display.flip()

pygame.quit()
