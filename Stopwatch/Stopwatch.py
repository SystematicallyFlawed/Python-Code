# Imports#
import pygame

pygame.init()

# Variables#
x = 400
y = 200

white = [255, 255, 255]
black = [0, 0, 0]

font = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()
frame_count = 0


# Display Setup#
display = pygame.display.set_mode([x, y])
pygame.display.set_caption("ITS A STOPWATCH")

# While running loop#
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    #Display Color#
    display.fill(white)

    #Timer Set Up#
    total_seconds =  frame_count // 60
    hours = total_seconds // 3600
    minutes = total_seconds // 60
    seconds = total_seconds - (minutes * 60)

    output_string = "Time Passed: " + str(hours) + ":" + str(minutes) + ":" + str(seconds)
    text = font.render(output_string, True, black)
    text_rect = text.get_rect(center=(x / 2, y / 2))
    display.blit(text, text_rect)

    frame_count += 1
    clock.tick(60)

    pygame.display.flip()

pygame.quit()