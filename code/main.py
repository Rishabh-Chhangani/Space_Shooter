import pygame
from os.path import join


# Genearl Setup
pygame.init()
Window_Width , Window_Height = 800 , 600
display_surface = pygame.display.set_mode((Window_Width , Window_Height))
running = True 
pygame.display.set_caption('SPACE SHOOTER')

# Plain Surface 
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# Importing an Image
player_surf = pygame.image.load(join('images','player.png'))

while running:
    # event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the game
    display_surface.fill('Grey')
    x += 0.1
    display_surface.blit(player_surf,(x,150))
    pygame.display.update()

pygame.quit()