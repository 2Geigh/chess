import pygame
from pygame.locals import *
pygame.init()

#dimensions and attributes for the game's viewport window
window_width = 500 #px
window_height = 500 #px
window_title = "Chess"

#boolean status that when toggled to False closes the viewport window
window_run_status = True

#creating the viewport window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)

TILE_WHITE = (200,200,200)
TILE_BLACK = (50,50,50)
tile_colour = (0,0,0)

TILE_WIDTH = window_width / 8
TILE_HEIGHT = TILE_WIDTH
tile_x = 0
tile_y = 0


#Generate the checker pattern
for l in range(0,8):
    if l % 2 != 0:
        for i in range(0, 8):
            if i % 2 != 0:
                tile_colour = TILE_BLACK
            else:
                tile_colour = TILE_WHITE

            pygame.draw.rect(window, tile_colour, [tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT], 50) #left, top, width, height
            tile_x += window_width / 8
    else:
        for i in range(0, 8):
            if i % 2 != 0:
                tile_colour = TILE_WHITE
            else:
                tile_colour = TILE_BLACK

            pygame.draw.rect(window, tile_colour, [tile_x, tile_y, TILE_WIDTH, TILE_HEIGHT], 50) #left, top, width, height
            tile_x += window_width / 8

    tile_y += window_height / 8
    tile_x = 0

pygame.display.flip()


#keep viewport window open if game is running
while (window_run_status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_run_status = False

pygame.quit()
quit()
