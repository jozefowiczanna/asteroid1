import pygame, sys

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids")

bg_surf = pygame.image.load('asteroid/graphics/background.png').convert()
ship_surf = pygame.image.load('asteroid/graphics/ship.png').convert_alpha()

font = pygame.font.Font('asteroid/graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((100,100,100))
    display_surface.blit(bg_surf, (0,0))
    display_surface.blit(ship_surf, (100,50))
    display_surface.blit(text_surf, (400,300))
    pygame.display.update()

    