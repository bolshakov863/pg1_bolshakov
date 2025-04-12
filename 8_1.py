import pygame
pygame.init()

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование линий")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)
points = []
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)

        screen.fill(BACKGROUND)

        for i in range(len(points) - 1):
            start_point = points[i]
            end_point = points[i + 1]
            pygame.draw.line(screen, (255,255,255), start_point, end_point, 3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()