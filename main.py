import pygame
from sys import exit
from datetime import datetime

pygame.init()

windowWidth = 800
windowHeight = 400
screen = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('Test Application')
pygame_icon = pygame.image.load('/Users/caleb/IdeaProjects/untitled2/Logo.png')
pygame.display.set_icon(pygame_icon)

test_font = pygame.font.Font('/Users/caleb/IdeaProjects/untitled2/Debrosee.ttf', 50)
text_surface = test_font.render('Test Application', True, 'White')
text_rect = text_surface.get_rect(center=(windowWidth / 2, windowHeight / 2))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(text_surface, text_rect)

    # current_time = datetime.now().strftime("%H:%M:%S")
    # print(current_time)

    pygame.display.update()
    clock.tick(60)

    # https://www.youtube.com/watch?v=AY9MnQ4x3zk
