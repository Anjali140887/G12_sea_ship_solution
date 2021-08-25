import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=500
height=400
screen = pygame.display.set_mode((width,height))

#load images
images={}
images["bg"] = pygame.image.load("sea.png").convert_alpha()
images["ship"] = pygame.image.load("ship.png").convert_alpha()

#variable to hold x-axis value of background image
bgx=0

while True:    
    screen.fill((50,150,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #decrement bgx to move the background
    bgx=bgx-5
    
    # Add code to reset bgx to 0 after bgx becomes less then -1000
    if   bgx < -1000  :
        bgx=0
    
    #display the background and ship image
    screen.blit(images["bg"],[bgx,0])
    screen.blit(images["ship"],[100,150])  
    
   
    pygame.display.update()
    clock.tick(30)
