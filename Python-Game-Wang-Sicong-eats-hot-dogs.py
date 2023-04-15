import random
import time
import sys
import pygame
from pygame.locals import *
from PIL import  Image
# 首先缩小游戏背景图片尺寸
img = Image.open(r'C:\Users\timberman\Pictures\Screenshots\background.jpg')
out = img.resize((800, 600) , Image.ANTIALIAS)
out.save(r'C:\Users\timberman\Pictures\Screenshots\background_resize.jpg')
 
width = 800
height = 600
pygame.init()
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('王思聪吃热狗(双人版)')
background = pygame.image.load(r'C:\Users\timberman\Pictures\Screenshots\background_resize.jpg').convert()
hotdogImg = pygame.image.load(r'C:\Users\timberman\Pictures\Screenshots\hotdog.png').convert_alpha()
wangImg = pygame.image.load(r'C:\Users\timberman\Pictures\Screenshots\wang.png').convert_alpha()
 
count1 = 0
count2 = 0
font = pygame.font.SysFont("arial",40)
player1_score = font.render("player1 score:%d" %(count1), True, (255, 255, 255))
player2_score = font.render("player2 score:%d" %(count2), True, (255, 255, 255))
 
w_width = wangImg.get_width() - 5
w_height = wangImg.get_height() - 5
h_width = hotdogImg.get_width() - 5
h_height = hotdogImg.get_height() - 5
fpsClock = pygame.time.Clock()
 
class Wang1:
    def __init__(self):
        self.power = 200
        self.x = random.randint(0, width-w_width)
        self.y = random.randint(0, height-w_height)
 
    def move(self, new_x, new_y):
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > width:
            self.x = 0
        else:
            self.x = new_x
        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > height:
            self.y = 0
        else:
            self.y = new_y
        self.power -= 10
 
    def eat(self):
        self.power += 20
        if self.power > 200:
            self.power = 200
 
class Wang2:
    def __init__(self):
        self.power = 200
        self.x = random.randint(0, width-w_width)
        self.y = random.randint(0, height-w_height)
 
    def move(self, new_x, new_y):
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > width:
            self.x = 0
        else:
            self.x = new_x
        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > height:
            self.y = 0
        else:
            self.y = new_y
        self.power -= 10
 
    def eat(self):
        self.power += 20
        if self.power > 200:
            self.power = 200
 
class Hotdog:
    def __init__(self):
        self.x = random.randint(0, width - h_width)
        self.y = random.randint(0, height - h_height)
 
    def move(self):
        new_x = self.x + random.choice([-10])
        if self.x < 0:
            self.x = width
        else:
            self.x = new_x
 
wang1 = Wang1()
wang2 = Wang2()
pygame.display.update()
hotdog = []
for item in range(random.randint(10,40)):
    newHotdog = Hotdog()
    hotdog.append(newHotdog)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                wang1.move(wang1.x - 10, wang1.y)
            if event.key == pygame.K_RIGHT:
                wang1.move(wang1.x + 10, wang1.y)
            if event.key == pygame.K_UP:
                wang1.move(wang1.x, wang1.y - 10)
            if event.key == pygame.K_DOWN:
                wang1.move(wang1.x, wang1.y + 10)
            if event.key == pygame.K_a:
                wang2.move(wang2.x - 10, wang2.y)
            if event.key == pygame.K_d:
                wang2.move(wang2.x + 10, wang2.y)
            if event.key == pygame.K_w:
                wang2.move(wang2.x, wang2.y - 10)
            if event.key == pygame.K_s:
                wang2.move(wang2.x, wang2.y + 10)
 
    screen.blit(background, (0, 0))
    screen.blit(player2_score, (580, 20))
    screen.blit(player1_score, (0, 20))
    for item in hotdog:
        screen.blit(hotdogImg, (item.x, item.y))
        item.move()
    screen.blit(wangImg, (wang1.x, wang1.y))
    screen.blit(wangImg, (wang2.x, wang2.y))
 
    if wang1.power < 0:
        print("Player2 Win!")
        pygame.display.update()
        time.sleep(1)
        sys.exit(0)
    if wang2.power < 0:
        print("Player1 Win!")
        pygame.display.update()
        time.sleep(1)
        sys.exit(0)
    elif len(hotdog) == 0:
        if player1_score > player2_score:
            print("Player1 Win!")
        else:
            print("Player2 Win!")
        pygame.display.update()
        sys.exit(0)
    for item in hotdog:
        if  ((wang1.x < item.x + w_width) and (wang1.x + w_width > item.x)
            and (wang1.y < item.y + h_height) and (w_height + wang1.y > item.y)) :
            hotdog.remove(item)
            count1 = count1 + 1
            player1_score = font.render("player1 score:%d" % count1, True, (255, 0, 0))
    for item in hotdog:
        if  ((wang2.x < item.x + w_width) and (wang2.x + w_width > item.x)
            and (wang2.y < item.y + h_height) and (w_height + wang2.y > item.y)) :
            hotdog.remove(item)
            count2 = count2 + 1
            player2_score = font.render("player2 score:%d" % count2, True, (255, 0, 0))
 
    pygame.display.update()
    fpsClock.tick(10)
