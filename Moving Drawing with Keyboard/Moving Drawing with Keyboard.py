#Imports#
import pygame
pygame.init()

#Inputs#
side_choice = int(input("How long do you want the sides of the box? "))

#Variables#
x = 1000
y = 800

white = (255,255,255)
black = (0,0,0)

side = side_choice
#Starts box in the middle no matter how big#
box_x = x / 2 - (side / 2)
box_y = y / 2 - (side / 2)

clock = pygame.time.Clock()

#Display set up#
display = pygame.display.set_mode([x,y])
pygame.display.set_caption("MOVE THE BOX")

#While running loop#
game_running = True
while game_running:
    #Event handling#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    #Moves the box when WASD are pressed#
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        box_x -= 20
    if keys[pygame.K_d]:
        box_x += 20
    if keys[pygame.K_w]:
        box_y -= 20
    if keys[pygame.K_s]:
        box_y += 20

    box_x = max(0,min(x - side, box_x))
    box_y = max(0,min(y - side, box_y))

    display.fill(white)
    pygame.draw.rect(display,black,[box_x,box_y,side,side])

    pygame.display.update()
    clock.tick(60)

pygame.quit()