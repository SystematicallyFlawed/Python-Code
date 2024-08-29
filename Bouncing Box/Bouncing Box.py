#Imports#
import pygame
pygame.init()

#Inputs#
speed_x_input = int(input("How fast should the box move on the x coordinate? "))
speed_Y_input = int(input("How fast should the box move on the y coordinate? "))
x_input = int(input("How many pixels wide should the box's confinement be? "))
y_input = int(input("How many pixels tall should the box's confinement be? "))

#Variables#
x = x_input
y = y_input
rect_x = 0
rect_y = 0
rect_length= 50
rect_height = 50
speed_x = speed_x_input
speed_y = speed_Y_input

blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

clock = pygame.time.Clock()

#Display set up#
display = pygame.display.set_mode([x,y])
pygame.display.set_caption("BOUNCING BOX?")

#While running loop#
game_running = True
while game_running:
    #So it will respond when you click on the window#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    display.fill(white)
    pygame.draw.rect(display, blue, [rect_x,rect_y,rect_length,rect_height])

    rect_x = rect_x + speed_x
    rect_y = rect_y + speed_y
    if rect_x > x - rect_length or rect_x < 0:
        speed_x = speed_x * -1
    if rect_y > y - rect_height or rect_y < 0:
        speed_y = speed_y * -1

    clock.tick(60)
    pygame.display.update()

#Handles the game closing, properly#
pygame.quit()