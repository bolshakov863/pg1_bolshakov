import pygame
pygame.init()

def move_towards(pos1, pos2, speed):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > speed:
        if dx > 0:
            x1 += speed
        else:
            x1 -= speed
    else:
        x1 = x2

    if abs(dy) > speed:
        if dy > 0:
            y1 += speed
        else:
            y1 -= speed
    else:
        y1 = y2

    return(x1, y1)

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Перемещение круга")

BACKGROUND = (0, 0, 0)
CIRCLE_COLOR = (255, 255, 255)
CIRCLE_RADIUS = 20

circle_pos = (320, 240)
speed = 3

clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    circle_pos = move_towards(circle_pos, mouse_pos, speed)

    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, CIRCLE_COLOR,
                       (int(circle_pos[0]),
                       int(circle_pos[1])),
                       CIRCLE_RADIUS)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()