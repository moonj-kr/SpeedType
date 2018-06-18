import pygame, time, random, eztext
from ScrapTestFiles.Type import text_objects

pygame.init()

# variables
lst = []
display_width = 1000
display_height = 800
h=display_height
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)
GOLD=(250,250,210)
EMERALD=(204,255,210)
LAVENDER=(230,230,250)
SALMON=(220,20,60)

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
    window.fill(BLACK)
    pygame.draw.line(window, SALMON, (30, 0), (30, display_height / 1.2), 10)
    pygame.draw.rect(window, GOLD, ((0, 0), (30, display_height / 1.2)))
    pygame.draw.line(window,SALMON , (display_width-30, 0), (display_width - 30, display_height / 1.2), 10)
    pygame.draw.rect(window,GOLD,((display_width-30,0), (30, display_height/1.2)))
    pygame.draw.line(window, BLUE, (0, display_height/1.2), (display_width, display_height/1.2), 4)
    window.blit(word,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

# fn that shows user input
def show_input(events):
    textbox.set_pos(display_width / 9.5, display_height / 1.09)
    textbox.update(events)
    pygame.draw.rect(window, WHITE, ((display_width/10, display_height / 1.1), (display_width/3, 35))) # input box!!
    textbox.draw(window)
    pygame.display.flip()


# fn that shows user input
def show_input_more(events, textbox):
    textbox.set_pos(display_width/9.5, display_height/1.08)
    textbox.update(events)
    pygame.draw.rect(window, WHITE, ((display_width / 10, display_height / 1.1), (display_width / 3, 35))) # input box!!
    textbox.draw(window)
    pygame.display.flip()

################ Window Setup ###################

# window setup
font = pygame.font.SysFont("Veranda", 30)
word=return_word()
text_surface = font.render(word, False, WHITE)
window = pygame.display.set_mode((display_width,display_height),pygame.RESIZABLE)
pygame.display.set_caption("Type the hella outta me")
clock = pygame.time.Clock()
pygame.draw.rect(window, WHITE, ((display_width/10, display_height / 1.1), (display_width/3, 35)))
pygame.display.update()
textbox = eztext.Input(maxlength=70, color=(BLACK), prompt='')

################ Game Loop ###################
def game_loop():
    input_word = ""
    word_height = 0
    crashed = False
    global display_width
    global display_height
    # display_width = 1000

    word_width = random.randint(50, display_width//1.05)
    current_score=0
    word = return_word()
    text_surface = font.render(word, False, WHITE)

    while crashed == False:
        events = pygame.event.get()
        word_display(text_surface, word_width, word_height)
        for event in events:
            # window exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.VIDEORESIZE:
                display_width, display_height = event.w, event.h
                pygame.display.set_mode((display_width,display_height),pygame.RESIZABLE)
        # word display
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    input_word += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    input_word = input_word[:-1]
                if(event.key==pygame.K_RETURN):
                    if input_word!=word :
                        print("failed, your score is :", current_score)
                        pygame.quit()
                        quit()
                    else:
                        if len(lst) == 0:
                            print("Congrats, you have finished the game")
                            pygame.quit()
                            quit()
                        else:
                            print("success")
                            current_score= current_score + len(word)
                            word = return_word()
                            text_surface = font.render(word, False, WHITE) # falling words

                            textbox = eztext.Input(maxlength=70, color=(BLACK), prompt='')
                            # clear window
                            # reset eztext

                            word_width = random.randint(50, display_width//1.05)
                            input_word = ""
                            word_height = 0
                            #time.sleep(0.5)
                            continue
        # update window
        show_input(events)
        pygame.display.update()
        word_height += 1
        time.sleep(0.01)

        # bordery
        if word_height > (display_height/1.2) -10:
            print("You've crashed")
            largeText = pygame.font.Font("freesansbold.ttf", 115)
            TextSurf, TextRect = text_objects("You've crashed", largeText)
            TextRect.center = (display_width / 2, display_height / 2)
            window.blit(TextSurf, TextRect)

            pygame.draw.rect(window, WHITE, ((display_width / 10, display_height / 1.1), (display_width / 3, 35)))

            pygame.display.update()
            time.sleep(0.01)
            pygame.quit()
            quit()

        # fps
        clock.tick(200)

if __name__ == '__main__':
    game_loop()
    pygame.quit()
    quit()
