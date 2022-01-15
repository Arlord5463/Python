import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    clock.tick(FPS)
pygame.quit()