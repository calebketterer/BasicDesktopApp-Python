import pygame
from sys import exit
from datetime import datetime

# initialize pygame
pygame.init()

# set window parameters
windowWidth = 800
windowHeight = 400
screen = pygame.display.set_mode((windowWidth, windowHeight))  # , pygame.FULLSCREEN for fullscreen

# load and set the game's icon
pygame.display.set_caption('Test Application')
pygame_icon = pygame.image.load('Graphics/Logo.png')
pygame.display.set_icon(pygame_icon)

# load and set the font
test_font = pygame.font.Font('Graphics/Debrosee.ttf', 50)
text_surface = test_font.render('Test Application', True, 'White')
text_rect = text_surface.get_rect(center=(windowWidth / 2, windowHeight / 2))

# load and set the background
background_surface = pygame.image.load('Graphics/Static-Background.png')
background_surface = pygame.transform.scale(background_surface, (windowWidth,windowHeight))
background_rect = background_surface.get_rect(center=(windowWidth / 2, windowHeight / 2))

# load and set the font
current_time = datetime.now().strftime("%H:%M:%S")
time_font = pygame.font.Font('Graphics/Debrosee.ttf', 50)
time_surface = time_font.render(f'Time: {current_time}', True, 'White')
time_rect = time_surface.get_rect(center=(windowWidth / 2, windowHeight / 2))

# clock controlling the refresh rate
clock = pygame.time.Clock()

# the render loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # adds the text and background to the display
    screen.blit(text_surface, text_rect)
    screen.blit(background_surface, background_rect)

    # first attempts to display the time
    # current_time = datetime.now().strftime("%H:%M:%S")
    # print('Current Time:', current_time)
    # screen.blit(time_surface, time_rect)

    # updates display at 60 fps
    pygame.display.update()
    clock.tick(60)

    # https://www.youtube.com/watch?v=AY9MnQ4x3zk
