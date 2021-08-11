import pygame as p
import random as r
import math
from pygame import mixer


p.init()

screen = p.display.set_mode((600,400))
background = p.image.load("bg.png")

running = True

p.display.set_caption("Game01")
icon  = p.image.load("a.png")
p.display.set_icon(icon)
dist = 0
score = 0



mixer.music.load('song.mp3')
mixer.music.play(-1)

font = p.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

over_font = p.font.Font('freesansbold.ttf',64)




#*******************************************************************************

playerImg = p.image.load("plane.png")
playerX = 300
playerY = 350
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no = 5

for i in range(no):
   enemyImg.append(p.image.load("enemy.png"))
   enemyX.append(r.randint(0,600))
   enemyY.append(r.randint(0,50))
   enemyX_change.append(2.1)
   enemyY_change.append(15)


bulletImg = p.image.load("bullet.png")
bulletX = 0
bulletY = 350
bulletX_change = 0
bulletY_change = 15
bullet_state ="ready" 

#*******************************************************************************
#functions

def player(X,Y):
    screen.blit(playerImg,(X,Y))
    
def enemy(X,Y,i):
    screen.blit(enemyImg[i],(X,Y))    

def bullet_fire(X,Y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(X,Y)) 

def col(enemyX,enemyY,bulletX,bulletY):
    dist = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if dist <= 20:
        return True
    else:
        return False
      
def game_over_text():
   xyz = over_font.render("!GAME-OVER!"  +str(score),True,(255,255,255))
   screen.blit(xyz,(50,200))

def score_text(x,y):
   xy = font.render("Score: "+str(score),True,(255,255,255))
   screen.blit(xy,(x,y))


                
#********************************************************************************
        
while running:

          screen.fill((0,0,0))
          screen.blit(background,(0,0))

   #buttons
   #******************************************************************************* 



          for event in p.event.get():
                  if event.type == p.QUIT:
                     running = False

                  if event.type == p.KEYDOWN:
                     
                        if event.key == p.K_LEFT:
                              if score <= 15:
                                     px = 2.4
                                     ex = 2.1

                              if score > 15 :
                                  px = 2.8
                                  ex = 2.5
                              if score > 25 :
                                  px = 3.6
                                  ex = 3.3                                  
                              if score > 50 :
                                  px = 5.0
                                  ex = 4.7

                              playerX_change = -px

                        if event.key == p.K_RIGHT:
                              if score <= 15:
                                     px = 2.4
                                     ex = 2.1

                              if score > 15 :
                                  px = 2.8
                                  ex = 2.5
                              if score > 25 :
                                  px = 3.6
                                  ex = 3.3                                  
                              if score > 50 :
                                  px = 5.0
                                  ex = 4.7


                              playerX_change = +px

                        if event.key == p.K_SPACE:
                           if bullet_state is "ready":
                               bulletX = playerX
                               bullet_fire( bulletX , bulletY )
                            

                                
                  if event.type == p.KEYUP:
                        if event.key == p.K_LEFT or event.key == p.K_RIGHT:
                            playerX_change = 0

         #******************************************************************************* 
         #conditions 
           

                
          playerX += playerX_change
          
          if playerX <= 0:
              playerX = 0
          if playerX >= 568:
              playerX = 568

          for i in range(no):
             enemyX[i] += enemyX_change[i]

             if enemyY[i] >= 270:
                   for j in range(no):
                         enemyY[j] = 3000
                         playerY = 1000
                   game_over_text()
                   break
             
             if enemyX[i] <= 0:
                              if score <= 15:
                                     px = 2.4
                                     ex = 2.1

                              if score > 15 :
                                  px = 2.8
                                  ex = 2.5
                              if score > 25 :
                                  px = 3.6
                                  ex = 3.3                                  
                              if score > 50 :
                                  px = 5.0
                                  ex = 4.7

                              enemyX_change[i] = ex                
                              enemyY[i] += enemyY_change[i] 
                 
             if enemyX[i] >= 568:
                              if score <= 15:
                                     px = 2.4
                                     ex = 2.1
                                     
                              if score > 15 :
                                  px = 2.8
                                  ex = 2.5
                              if score > 25 :
                                  px = 3.6
                                  ex = 3.3                                  
                              if score > 50 :
                                  px = 5.0
                                  ex = 4.7
                              if 10 <= score >= 5 :
                                  px = 5.0
                                  ex = 4.0

                              enemyX_change[i] = -ex                
                              enemyY[i] += enemyY_change[i] 
             

             coln = col(enemyX[i],enemyY[i],bulletX,bulletY)
             if coln:
                 explosion = mixer.Sound('Explosion.wav')
                 explosion.play()
                 bulletY = 300
                 bullet_state = "ready"
                 score += 1
                 #print(score)
                 enemyX[i] = r.randint(200,400)
                 enemyY[i] = r.randint(0,10)

             enemy(enemyX[i],enemyY[i],i)

                     
          if bulletY <= 0:
              bulletY = 300
              bullet_state = "ready"

          
          if bullet_state is "fire":
                bullet_fire(bulletX,bulletY)
                bulletY -= bulletY_change

             
          player(playerX,playerY)
          score_text(textX,textY)
          p.display.update()
#*******************************************************************************
