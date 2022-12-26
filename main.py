import pygame, sys

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

bg_surf = pygame.image.load('asteroid/asteroid1/graphics/background.png').convert()
ship_surf = pygame.image.load('asteroid/asteroid1/graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

font = pygame.font.Font('asteroid/asteroid1/graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT))

while True:

    # 1. input -> events (mouse click, mouse movement, press of a button, controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # framerate limit
    clock.tick(120)

    # mouse input
    # place the ship on the mouse position while using the methods
    ship_rect.center = pygame.mouse.get_pos()
    # 2. updates
    display_surface.fill((100,100,100))
    display_surface.blit(bg_surf, (0,0))
    # if the top of the ship is at the top of the window -> stop the movement
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)
    pygame.display.update()