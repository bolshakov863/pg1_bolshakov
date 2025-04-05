import math


import pygame
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Моя игра")
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)

BUTTON_COLOR = (0, 191, 255)
HOVER_COLOR = (0, 140, 255)
CLICK_COLOR = (0, 50, 255)
BACKGROUND_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_RADIUS = 50
BUTTON_CENTER = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
hovering = False
clicking = False

button_rect = pygame.Rect(BUTTON_CENTER[0] - BUTTON_RADIUS,
                          BUTTON_CENTER[1] - BUTTON_RADIUS,
                          BUTTON_RADIUS * 2, BUTTON_RADIUS * 2)

FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            if button_rect.collidepoint(event.pos):
                hovering = True
            else:
                hovering = False

            if clicking:
                BUTTON_CENTER[0] = event.pos[0]
                BUTTON_CENTER[1] = event.pos[1]

            if hovering:
                button_color = HOVER_COLOR
            else:
                button_color = BUTTON_COLOR



        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3 and button_rect.collidepoint(event.pos):
                clicking = True
            else:
                clicking = False

 #       screen.fill(BACKGROUND)

        if clicking:
            button_color = CLICK_COLOR
        elif hovering:
            button_color = HOVER_COLOR
        else:
            button_color = BUTTON_COLOR



    pygame.draw.circle(screen, button_color, BUTTON_CENTER, BUTTON_RADIUS)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
