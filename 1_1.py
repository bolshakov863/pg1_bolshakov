import random
from all_colors import *
import pygame
pygame.init()

#pygame.mixer.init()
#pygame.mixer.music.load('resurs/La la land.mp3')
#pygame.mixer.music.play(-1)

size = (0, 0)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)
#FPS = 60
clock = pygame.time.Clock()
COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]
running = True
timer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color_index = random.randint(0, 18)
    if color_index == 18:
      BACKGROUND = (random.randint(0, 225), random.randint(0,255), random.randint(0,255))
    else:
      BACKGROUND = COLORS[color_index]
    screen.fill(BACKGROUND)
    pygame.display.flip()
    pygame.time.delay(random.randint(200, 800))


pygame.quit()