import pygame, sys

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids")

# create a surface
test_surf = pygame.Surface((400,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((20,120,250))
    test_surf.fill((0,200,20))
    display_surface.blit(test_surf, (WINDOW_WIDTH - test_surf.get_width(),0))
    pygame.display.update()
    