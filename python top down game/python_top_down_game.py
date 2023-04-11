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
nsheep = 200
#images and fonts
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score:', True, (200, 200, 0))
text2 = font.render(str(score), True, (200, 200, 0))
text3 = font.render('YOU WIN!', True, (200, 200, 0))

#CONSTANTS (not required, just makes code easier to read)
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


class Sheep:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isa = True
        self.direction = [LEFT,RIGHT,UP,DOWN]
    def sheepMove(self,):
        if timer % 10 == 0: #only change direction every 50 game loops
            self.direction = random.randrange(0, 4) #set random direction

        if self.direction == LEFT and self.xpos >= 0:
            self.xpos-=8 #move left

        elif self.direction == RIGHT and self.xpos+80 <= 800:
            self.xpos += 8 #move right

        elif self.direction == UP and self.ypos >= 0:
            self.ypos -=8 #move up
        elif self.ypos+50 <= 800:
            self.ypos +=8 #move down

    def draw(self):
        SheepPic = pygame.image.load("sheep.jpg")
        if self.isa == True:
            screen.blit(SheepPic, (self.xpos, self.ypos,80,40))
    

pen: list[Sheep] = []

for i in range(nsheep):
    pen.append(Sheep(400,400))


#function defintions------------------------------------
#can you tell me what the parameters are for these functions, and what they return (if anything)?






#create sheep!
#numbers in list represent xpos, ypos, direction moving, and whether it's been caught or not!
#make more sheeps here!



#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity (left/right speed) of player
vy = 0 #y velocity (up/down speed) of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

while score < nsheep: #GAME LOOP############################################################
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

    if xpos <= 0:
        xpos = 0
    elif xpos >= 760:
        xpos = 760
    elif ypos <= 0:
        ypos = 0
    elif ypos >= 760:
        ypos = 760
    
    
    
    #player/sheep collision!
        for i in range (len(pen)):
            if pen[i].isa == True:
                if pen[i].xpos > xpos:
                    if pen[i].xpos < xpos + 40:
                        if pen[i].ypos + 40 > ypos:
                            if pen[i].ypos+40 < ypos+40:
                                    pen[i].isa = False #catch da sheepies!#make it so this function can change this value
                                    score +=1

    #update player position
    xpos+=vx 
    ypos+=vy
    
    #update sheep position
    # RENDER
    # Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear

    for i in range(len(pen)):
        pen[i].sheepMove()
    for i in range(len(pen)):
        pen[i].draw()
    #draw player
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 40, 40))





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
