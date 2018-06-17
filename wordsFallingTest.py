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
    pygame.draw.line(window, (0, 0, 255), (0, 700), (1000, 700), 4)
    window.blit(word,(x,y))

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
def show_input(events):
    textbox.set_pos(105, 740)
    textbox.update(events)
    pygame.draw.rect(window, white, ((100, 735), (250, 30))) # input box!!
    textbox.draw(window)
    pygame.display.flip()


# fn that shows user input
def show_input_more(events, textbox):
    textbox.set_pos(105, 740)
    textbox.update(events)
    pygame.draw.rect(window, white, ((100, 735), (250, 30))) # input box!!
    textbox.draw(window)
    pygame.display.flip()

################ Window Setup ###################

# window setup
font = pygame.font.SysFont("Veranda", 30)
word=return_word()
text_surface = font.render(word, False, white)
window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Speed Type")
clock = pygame.time.Clock()
pygame.draw.rect(window, white, ((100, 735), (250, 30)))
pygame.display.update()
textbox = eztext.Input(maxlength=70, color=(black), prompt='')

################ Game Loop ###################
def game_loop():
    input_word = ""
    word_height = 0
    crashed = False
    x = random.randint(50, 950)
    current_score=0
    word = return_word()
    text_surface = font.render(word, False, white)

    while crashed == False:
        events = pygame.event.get()
        word_display(text_surface, x, word_height)
        for event in events:
            # window exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
                            text_surface = font.render(word, False, white) # falling words

                            textbox = eztext.Input(maxlength=70, color=(black), prompt='')
                            # clear window
                            # reset eztext

                            x = random.randint(50, 950)
                            input_word = ""
                            word_height = 0
                            #time.sleep(0.5)
                            continue
        # update window
        show_input(events)
        pygame.display.update()
        word_height += 0.25

        # bordery
        if word_height > 690:
            print("You've crashed")
            largeText = pygame.font.Font("freesansbold.ttf", 115)
            TextSurf, TextRect = text_objects("You've crashed", largeText)
            TextRect.center = (display_width / 2, display_height / 2)
            window.blit(TextSurf, TextRect)

            pygame.draw.rect(window, white, ((100, 735), (250, 30)))

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
