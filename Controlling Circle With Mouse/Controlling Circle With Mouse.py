#Imports#
import pygame
pygame.init()

#Variables#
x = 600
y = 500

white = (255,255,255)
blue = (0,0,255)

clock = pygame.time.Clock()

#Mouse position set up#
pygame.mouse.set_visible(0)

#Display set up#
display = pygame.display.set_mode([x,y])
pygame.display.set_caption("MOUSE MOVE CIRCLE")

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

    display.fill(white)
    pygame.draw.circle(display,blue,(mouse_x,mouse_y),50)

    pygame.display.update()
    clock.tick(60)

pygame.quit()