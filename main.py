import pygame, sys

# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

# background
bg_surf = pygame.image.load('asteroid/asteroid1/graphics/background.png').convert()

# ship import
ship_surf = pygame.image.load('asteroid/asteroid1/graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

# text import
font = pygame.font.Font('asteroid/asteroid1/graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 50))

# laser import
laser_surf = pygame.image.load('asteroid/asteroid1/graphics/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)

# drawing
test_rect = pygame.Rect(100, 200, 300, 400)

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # framerate limit
    clock.tick(120)

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # update
    laser_rect.y -= 4

    # drawing
    display_surface.fill((100,100,100))
    display_surface.blit(bg_surf, (0,0))
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(text_surf, text_rect)
    display_surface.blit(laser_surf, laser_rect)

    pygame.draw.rect(display_surface,'white',text_rect.inflate(30,30),width=5,border_radius=10)
    pygame.draw.lines(display_surface,'pink',True,[(300,50),(700,100),(600,200)],width=5)

    # draw the final frame
    pygame.display.update()