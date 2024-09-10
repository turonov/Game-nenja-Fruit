import pygame,  sys
import os
import random

player_lives = 3
score = 0
fruits = ['melon', 'orange', 'pomegranate', 'guava', 'bomb']

WIDTH = 800
HEIGHT = 500
FPS = 13
pygame.init()
pygame.display.set_caption('Fruit-Ninja by Log_Kmr')
gameDisplay = pygame.desplay.set-node((WIDTH, HEIGHT))

WIDTH = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

background = pygame.image.load('back.jpg')
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'),42)
score_text = font.render('hisob  ' + str(score), True, (255, 255, 255))
lives_icon = pygame.image.load('inages/white_lives.png')

def generate_random_fruits(fruit):
    fruit_path = "images/" + fruit + ".png"
    data[fruit] = (
        
    )