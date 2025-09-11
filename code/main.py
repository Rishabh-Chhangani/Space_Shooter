import pygame
from os.path import join
from random import randint


# Genearl Setup
pygame.init()
Window_Width , Window_Height = 1280 , 660
display_surface = pygame.display.set_mode((Window_Width , Window_Height))
running = True 
pygame.display.set_caption('SPACE SHOOTER')

# Plain Surface 
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# Importing an Image
player_surf = pygame.image.load(join('images','player.png')).convert_alpha()
player_rect = player_surf.get_frect(center=(Window_Width / 2,Window_Height / 2))
player_direction = 1

star_surf = pygame.image.load(join('images','star.png')).convert_alpha()
star_pos = [(randint(0,Window_Width),randint(0,Window_Height)) for i in range(20)]

meteor_surf = pygame.image.load(join('images' , 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (Window_Width / 2,Window_Height / 2))

laser_surf = pygame.image.load(join('images' , 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(center =( 20 , Window_Height - 40 ))


# Game Loop
while running:
    # event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the game
    display_surface.fill('darkgray') 
    for pos in star_pos:
        display_surface.blit(star_surf,pos)
    
    display_surface.blit(meteor_surf,meteor_rect)
    display_surface.blit(laser_surf , laser_rect)


    player_rect.x += player_direction * 0.3
    if player_rect.right > Window_Width or player_rect.left < 0:
        player_direction *= -1
    # if player_rect.right < Window_Width:
    #     player_rect.left += 0.2
    display_surface.blit(player_surf,player_rect)
   

    pygame.display.update()

pygame.quit()