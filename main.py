import pygame, sys
from random import randint, uniform

def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= round(dt * speed)
        if rect.bottom < 0:
            laser_list.remove(rect)

def meteor_update(meteor_list, speed = 300):
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * dt * speed
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)

def display_time():
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True, (255,255,255))
    text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 50))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (255,255,255), text_rect.inflate(30,30), width = 8, border_radius = 5)

def laser_timer(can_shoot, duration=500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

# background
bg_surf = pygame.image.load('../asteroid1/graphics/background.png').convert()

# ship import
ship_surf = pygame.image.load('../asteroid1/graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

# laser import
laser_surf = pygame.image.load('../asteroid1/graphics/laser.png').convert_alpha()
laser_list = []

# text import
font = pygame.font.Font('../asteroid1/graphics/subatomic.ttf', 50)

can_shoot = True
shoot_time = None

meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

meteor_surf = pygame.image.load('../asteroid1/graphics/meteor.png').convert_alpha()
meteor_list = []

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if can_shoot:
                laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
                laser_list.append(laser_rect)
                can_shoot = False
                shoot_time = pygame.time.get_ticks()
        if event.type == meteor_timer:
            # random position
            meteor_x = randint(-100, WINDOW_WIDTH + 100)
            meteor_y = randint(-100, -50)
            
            # creating a rect
            meteor_rect = meteor_surf.get_rect(center = (meteor_x, meteor_y))

            # create a random direction
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 1)
            meteor_list.append((meteor_rect, direction))

    # framerate limit
    dt = clock.tick(120) / 1000

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # update
    laser_update(laser_list)
    can_shoot = laser_timer(can_shoot, 500)
    meteor_update(meteor_list)

    # meteor ship collision
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            pygame.quit()
            sys.exit()

    # laser meteor collision
    for laser_rect in laser_list:
        for meteor_tuple in meteor_list:
            if laser_rect.colliderect(meteor_tuple[0]):
                meteor_list.remove(meteor_tuple)
                laser_list.remove(laser_rect)

    # drawing
    display_surface.fill((100,100,100))
    display_surface.blit(bg_surf, (0,0))
    display_surface.blit(ship_surf, ship_rect)
    for laser_rect in laser_list:
        display_surface.blit(laser_surf, laser_rect)
    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surf, meteor_tuple[0])

    display_time()

    # draw the final frame
    pygame.display.update()