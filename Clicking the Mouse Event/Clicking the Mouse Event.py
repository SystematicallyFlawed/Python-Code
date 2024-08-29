#Imports#
import pygame
pygame.init()

#Variables#
x = 600
y = 500

white = (255,255,255)
black = (0,0,0)

rect_x = 0
rect_y = 0

#Set up display#
display = pygame.display.set_mode([x,y])
pygame.display.set_caption("CLICKY CLICKY AND BOX MOVES?")

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect_x,rect_y = pygame.mouse.get_pos()
            rect_x -= 25
            rect_y -= 25

    display.fill(white)
    pygame.draw.rect(display,black,[rect_x,rect_y,50,50])

    pygame.display.update()

pygame.quit()