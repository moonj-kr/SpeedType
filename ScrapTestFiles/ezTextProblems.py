import pygame, time, random, eztext
from ScrapTestFiles.Type import text_objects

pygame.init()

# variables
lst = []
display_width = 1000
display_height = 800
black = (0,0,0)
white = (255, 255, 255)
green = (0,100,0)
#name = ""

def text_objects(text, font):
    textSurface = font.render(text,True, white)
    return textSurface, textSurface.get_rect()

# fn that shows user input
def show_input(events):
    textbox.set_pos(105, 740)
    textbox.update(events)
    pygame.draw.rect(window, white, ((100, 735), (250, 30))) # input box!!
    textbox.draw(window)
    pygame.display.flip()

def show_input_more(events, textbox):
    print(pygame.event.get())

    textbox.set_pos(105, 740)

    #pygame.event.clear()

    textbox.update(events)
    pygame.draw.rect(window, white, ((100, 735), (250, 30))) # input box!!
    textbox.draw(window)
    pygame.display.flip()

def text_score(text,font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

################ Window Setup ###################

# window setup
font = pygame.font.SysFont("Veranda", 30)
window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Speed Type")
clock = pygame.time.Clock()
pygame.draw.rect(window, white, ((100, 735), (250, 30)))
pygame.display.update()
textbox = eztext.Input(maxlength=70, color=(black), prompt='')

################ Game Loop ###################
def game_loop():
    crashed = False

    while crashed == False:
        events = pygame.event.get()

        for event in events:
            # window exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # word display
            if event.type == pygame.KEYDOWN:
                #show_input(events)
                if(event.key==pygame.K_RETURN):
                    print("success")
                    print(event.key)

                    pygame.draw.rect(window, white, ((100, 735), (250, 30)))
                    pygame.display.update()
                    textbox1 = eztext.Input(maxlength=70, color=(black), prompt='')
                    #show_input_more(events,textbox1)
                    pygame.display.update()

                    time.sleep(0.5)
                    continue
                #else:
                #    show_input(events)
        # update window
        show_input(events)
        pygame.display.update()

        # fps
        clock.tick(200)

if __name__ == '__main__':
    game_loop()
    pygame.quit()
    quit()
