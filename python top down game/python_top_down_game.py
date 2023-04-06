import pygame
import random

#set up pygame stuff
pygame.init()  
pygame.display.set_caption("top down game")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

#game variables
timer = 0 #used for sheep movement
score = 0

#images and fonts
SheepPic = pygame.image.load("sheep.jpg")
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score:', True, (200, 200, 0))
text2 = font.render(str(score), True, (200, 200, 0))
text3 = font.render('YOU WIN!', True, (200, 200, 0))

#CONSTANTS (not required, just makes code easier to read)
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

#function defintions------------------------------------
#can you tell me what the parameters are for these functions, and what they return (if anything)?
def sheepMove(position):
    if timer % 50 == 0: #only change direction every 50 game loops
        position[2] = random.randrange(0, 4) #set random direction

    if position[2] == LEFT and position[0] >= 0:
        position[0]-=8 #move left

    elif position[2] == RIGHT and position[0]+80 <= 800:
        position[0] += 8 #move right

    elif position[2] == UP and position[1] >= 0:
        position[1] -=8 #move up
    elif position[1]+50 <= 800:
        position[1] +=8 #move down
    return position

def collision(PlayerX, PlayerY, sheepInfo):
    if PlayerX+40 > sheepInfo[0]:
       if PlayerX < sheepInfo[0]+40:
           if PlayerY+40 >sheepInfo[1]:
               if PlayerY < sheepInfo[1]+40:
                   if sheepInfo[3] == False: #only catch uncaught sheeps!
                        sheepInfo[3] = True #catch da sheepies!
                        global score #make it so this function can change this value
                        score +=1



#create sheep!
#numbers in list represent xpos, ypos, direction moving, and whether it's been caught or not!
sheep1 = [200, 400, RIGHT, False]
sheep2 = [200, 400, LEFT, False]
sheep3 = [200, 400, UP, False]
sheep4 = [200, 400, DOWN, False]
sheep5 = [200, 300, LEFT, False]
#make more sheeps here!



#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity (left/right speed) of player
vy = 0 #y velocity (up/down speed) of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

while score<5: #GAME LOOP############################################################
    clock.tick(60) #FPS
    timer+=1
    
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        #check if a key has been PRESSED
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True

        #check if a key has been LET GO
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
          
    #physics
    #section--------------------------------------------------------------------
    
    #player movement!--------
    if keys[LEFT] == True:
        vx = -8
    elif keys[RIGHT] == True:
        vx = 8
    else:
        vx = 0
    if keys[UP] == True:
        vy = -8
    elif keys[DOWN] == True:
        vy = 8
    else:
        vy = 0


    #player/sheep collision!
    collision(xpos, ypos, sheep1)
    collision(xpos, ypos, sheep2)
    collision(xpos, ypos, sheep3)
    collision(xpos, ypos, sheep4)
    collision(xpos, ypos, sheep5)

    #update player position
    xpos+=vx 
    ypos+=vy
    
    #update sheep position
    sheep1 = sheepMove(sheep1)
    sheep2 = sheepMove(sheep2)
    sheep3 = sheepMove(sheep3)
    sheep4 = sheepMove(sheep4)
    sheep5 = sheepMove(sheep5)
    # RENDER
    # Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
  
    #draw player
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 40, 40))

    #draw sheep
    if sheep1[3] == False: #don't draw them if they're already caught!
        #pygame.draw.rect(screen, (250, 100, 100), (sheep1[0], sheep1[1], 40, 40)) #use this if you don't have a jpg
        screen.blit(SheepPic, (sheep1[0], sheep1[1]))
    
    if sheep2[3] == False: #don't draw them if they're already caught!
        #pygame.draw.rect(screen, (250, 100, 100), (sheep1[0], sheep1[1], 40, 40)) #use this if you don't have a jpg
        screen.blit(SheepPic, (sheep2[0], sheep2[1]))
    
    if sheep3[3] == False: #don't draw them if they're already caught!
        #pygame.draw.rect(screen, (250, 100, 100), (sheep1[0], sheep1[1], 40, 40)) #use this if you don't have a jpg
        screen.blit(SheepPic, (sheep3[0], sheep3[1]))

    if sheep4[3] == False: #don't draw them if they're already caught!
        #pygame.draw.rect(screen, (250, 100, 100), (sheep1[0], sheep1[1], 40, 40)) #use this if you don't have a jpg
        screen.blit(SheepPic, (sheep4[0], sheep4[1]))
    
    if sheep5[3] == False: #don't draw them if they're already caught!
        #pygame.draw.rect(screen, (250, 100, 100), (sheep1[0], sheep1[1], 40, 40)) #use this if you don't have a jpg
        screen.blit(SheepPic, (sheep5[0], sheep5[1]))




    #display score
    screen.blit(text, (20, 20))
    text2 = font.render(str(score), True, (200, 200, 0))#update score number
    screen.blit(text2, (140, 20))

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------

#end screen
screen.fill((0,0,0)) 
screen.blit(text3, (400,400))
pygame.display.flip()
pygame.time.wait(2000)#pause for a bit before ending

pygame.quit()
