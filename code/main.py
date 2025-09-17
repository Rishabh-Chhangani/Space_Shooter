import pygame
from os.path import join
from random import randint


# Genearl Setup
pygame.init()
Window_Width , Window_Height = 800 , 600
display_surface = pygame.display.set_mode((Window_Width , Window_Height))
pygame.display.set_caption('SPACE SHOOTER')
running = True 
clock = pygame.time.Clock()

# Plain Surface 
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# Importing an Image
player_surf = pygame.image.load(join('images','player.png')).convert_alpha()
player_rect = player_surf.get_frect(center=(Window_Width / 2,Window_Height / 2))
player_direction = pygame.Vector2(1,1)
player_speed = 300

star_surf = pygame.image.load(join('images','star.png')).convert_alpha()
star_pos = [(randint(0,Window_Width),randint(0,Window_Height)) for i in range(20)]

meteor_surf = pygame.image.load(join('images' , 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (Window_Width / 2,Window_Height / 2))

laser_surf = pygame.image.load(join('images' , 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(center =( 20 , Window_Height - 40 ))


# Game Loop
while running:
    dt = clock.tick() / 1000 #dt is dealt ta time 

    # event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #input
    # print(pygame.mouse.get_pressed())
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP]) 
    player_direction = player_direction.normalize() if player_direction else player_direction
    # In the above LOC is wriiten as when we move diagonaly the speed is 426 but while moving up/down or right/left it is 300 to make the diagonal speed equal to basic movement speed we added i the above line 
    player_rect.center += player_direction * player_speed * dt
    print(player_direction)

    # Draw the game
    display_surface.fill('darkgray') 
    for pos in star_pos:
        display_surface.blit(star_surf,pos)
    
    display_surface.blit(meteor_surf,meteor_rect)
    display_surface.blit(laser_surf , laser_rect)

    if player_rect.bottom >= Window_Height or player_rect.top <= 0:
        player_direction.y *= -1
    if player_rect.right >= Window_Width or player_rect.left <= 0:
        player_direction.x *= -1


    player_rect.center += player_direction * player_speed * dt
    display_surface.blit(player_surf,player_rect)
   

    pygame.display.update()

pygame.quit()