# typing test

# import stuff
import pygame
import eztext


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size_width = (1366)
size_height = (768)
gameDisplay = pygame.display.set_mode((size_width, size_height))

textbox = eztext.Input(maxlength=70, color=(WHITE), prompt='')

pygame.display.set_caption("Input Test")

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True

    gameDisplay.fill(BLACK)
    textbox.set_pos(50,300)
    textbox.update(events)
    textbox.draw(gameDisplay)



    mouse = pygame.mouse.get_pos()

    ##score prompt text
    displayScoreFont = pygame.font.Font('mini_pixel-7.ttf', 50)
    displayScoreText = displayScoreFont.render('Score:', 1, WHITE)
    gameDisplay.blit(displayScoreText, [1114, 54])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()











