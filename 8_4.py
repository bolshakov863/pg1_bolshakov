import pygame
pygame.init()

def remove_point(mouse_pos):
    for point in points:
        if ((point[0]-mouse_pos[0])**2 + (point[1]-mouse_pos[1])**2
                <= REMOVE_RADIUS**2):
            points.remove(point)
            break

def get_closest_point(mouse_pos):
    closest_point = None
    closest_distance = float('inf')
    for point in points:
        distance = ((point[0]-mouse_pos[0])**2 +
                    (point[1]-mouse_pos[1])**2)**0.5
        if distance <= POINT_RADIUS and distance < closest_distance:
            closest_point = point
            closest_distance = distance
    return closest_point

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Рисование линий")
BACKGROUND = (0, 0, 0)
screen.fill(BACKGROUND)
LINE_COLOR = (255, 255, 255)
PREVIEW_COLOR = (192, 192, 192)
HIGHLIGHT_COLOR = (255, 0, 0)
points = []
POINT_RADIUS = 5
REMOVE_RADIUS = 5
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    closest_point = get_closest_point(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        elif event.type == pygame.MOUSEBUTTONDOWN:
            if closest_point:
                if event.button == 3:
                   points.remove(closest_point)
                elif event.button == 1:
                   points.append(closest_point)
                   print(points)
            elif event.button == 1:
                mouse_pos = pygame.mouse.get_pos
                points.append(mouse_pos)



        screen.fill(BACKGROUND)


        for i in range(len(points) - 1):
            pygame.draw.line(screen, LINE_COLOR, points[i], points[i + 1], 3)

        if len(points) > 0:
            pygame.draw.aaline(screen, PREVIEW_COLOR, points[-1], mouse_pos, 3)

        if closest_point:
            pygame.draw.circle(screen, HIGHLIGHT_COLOR, closest_point, POINT_RADIUS, 1)



    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()