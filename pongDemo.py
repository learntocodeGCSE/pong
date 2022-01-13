import pygame, sys
from pygame.locals import *
import random
import time

pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255,0,0)

window = pygame.display.set_mode((500,600))
window.fill(WHITE)
pygame.display.set_caption("Game")

class Ball(pygame.sprite.Sprite):
    def __init__(self):
          super().__init__()
          self.image = pygame.image.load("ball.png")
          self.surf = pygame.Surface((10, 10))
          self.rect = self.surf.get_rect(center = (250,295))
          self.velocity = [random.randint(4,8), random.randint(-8,8)]

    def move(self):
           self.rect.x +=self.velocity[0]
           self.rect.y +=self.velocity[1]

    def wallCollision(self, scoreList):
        if self.rect.x > 500:
            self.velocity[0] = -self.velocity[0]

        if self.rect.x < 0:
            self.velocity[0] = -self.velocity[0]

        if self.rect.y <-30:
            self.velocity[1] = -self.velocity[1]
            self.rect.x = 250
            self.rect.y = 295
            self.velocity = [random.randint(4,8), random.randint(-8,8)]
            scoreList[1] += 1

        if self.rect.y > 630:
            self.velocity[1] = -self.velocity[1]
            self.rect.x = 250
            self.rect.y = 295
            self.velocity = [random.randint(4,8), random.randint(-8,8)]
            scoreList[0] += 1

        return scoreList

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, n):
        super().__init__()
        self.image = pygame.image.load("paddle.png")
        self.surf = pygame.Surface((64, 12))
        self.rect = self.surf.get_rect(center = (x,y))
        self.n = n
        self.score = 0

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.n == 1:
            if self.rect.left > 0:
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5,0)
                
            if self.rect.right < 500:
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5,0)


        if self.n == 2:
            if self.rect.left > 0:
                if pressed_keys[K_a]:
                    self.rect.move_ip(-5,0)
                
            if self.rect.right < 500:
                if pressed_keys[K_d]:
                    self.rect.move_ip(5,0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Background():
    def __init__(self):
        self.backgroundImage = pygame.image.load("backgroundImage.png")
        self.rectBGImage = self.backgroundImage.get_rect()
        self.bgX = 0
        self.bgY = 0

    def draw(self):
        window.blit(self.backgroundImage,(self.bgX, self.bgY))

background = Background()
P1 = Player(225, 20, 1)
P2 = Player(225, 580, 2)
ball = Ball()

playerList = [P1,P2]
scoreList = [0, 0]

font = pygame.font.SysFont("Verdana", 60)
fontSmall = pygame.font.SysFont("Verdana", 20)
fontXtraSmall = pygame.font.SysFont("Verdana", 10)

while True:
    background.draw()
    p1ScoreRendered = fontSmall.render("Score: "+str(scoreList[0]), True, WHITE)
    p2ScoreRendered = fontSmall.render("Score: "+str(scoreList[1]), True, WHITE)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    ball.wallCollision(scoreList)

    if pygame.sprite.spritecollideany(ball, playerList):
        ball.velocity[1] = -ball.velocity[1]

    ball.draw(window)
    ball.move()

    P1.update()
    P2.update()

    P1.draw(window)
    P2.draw(window)

    window.blit(p1ScoreRendered,(10,10))
    window.blit(p2ScoreRendered,(10,550))

    pygame.display.update()
    FramePerSec.tick(FPS)
    










        
        
            
        
