import pygame, sys

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

ship_y_pos = 500
bg_surf = pygame.image.load('asteroid/asteroid1/graphics/background.png').convert()
ship_surf = pygame.image.load('asteroid/asteroid1/graphics/ship.png').convert_alpha()


font = pygame.font.Font('asteroid/asteroid1/graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255,255,255))

while True:

    # 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # framerate limit
    clock.tick(120)

    # 2. updates
    display_surface.fill((100,100,100))
    display_surface.blit(bg_surf, (0,0))
    display_surface.blit(ship_surf, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    display_surface.blit(text_surf, (WINDOW_WIDTH/2, WINDOW_HEIGHT - 100))
    pygame.display.update()