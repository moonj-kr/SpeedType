import pygame, time, random
from pygame.locals import *
from Type import text_objects

pygame.init()

# variables
lst = []
display_width = 1000
display_height = 800
black = (0,0,0)
white = (255, 255, 255)

# fn to read file of words
def read_file():
    file = open("Wordlist.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        lst.append(line.strip())

# helper fn to return word
def return_word():
    read_file()
    return lst.pop(random.randint(0,len(lst)))

# fn that displays words
def word_display(word,x,y):
    window.fill(black)
    window.blit(word,(x,y))

# fn that message to player
def crashed():
    message_display("You ran out of time!")

def level_up():
    pass

# fn that shows text to player
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (display_width/2 , display_height/2)
    window.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def text_objects(text, font):
    textSurface = font.render(text,True, white)
    return textSurface, textSurface.get_rect()

# fn that shows user input
def show_input(value):
    pass

# fn that shows player's current level
def show_level():
    pass

# fn that shows the player score
def show_score():
    pass

################ Window Setup ###################

# window setup
font = pygame.font.SysFont("Veranda", 30)
text_surface = font.render(return_word(), False, white)
window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Speed Type")
clock = pygame.time.Clock()

################ Game Loop ###################
def game_loop():
    name = ""
    word_height = 0
    crashed = False

    while crashed == False:
        for event in pygame.event.get():
            # keep track of events
            print(event)

            # window exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # user typing display
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.key == K_RETURN:
                    name = ""
                print(name)

        # word display
        word_display(text_surface,display_width/2,word_height)

        # update window
        pygame.display.update()
        word_height += 50

        # border
        if word_height > 700:
            print("You've crashed")
            largeText = pygame.font.Font("freesansbold.ttf", 115)
            TextSurf, TextRect = text_objects("You've crashed", largeText)
            TextRect.center = (display_width / 2, display_height / 2)
            window.blit(TextSurf, TextRect)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            quit()


        # fps
        clock.tick(2)

if __name__ == '__main__':
    game_loop()
    pygame.quit()
    quit()
