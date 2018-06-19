import pygame, time, random, eztext
from ScrapTestFiles.Type import text_objects

pygame.init()

# variables
lst = []
display_width = 1000
display_height = 800
w=display_width
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

# fn that displays game borders
def word_display(word,x,y):
    window.fill(BLACK)
    pygame.draw.line(window, SALMON, (30, 0), (30, display_height / 1.2), 10)
    pygame.draw.rect(window, GOLD, ((0, 0), (30, display_height / 1.2)))
    pygame.draw.line(window,SALMON , (display_width-30, 0), (display_width - 30, display_height / 1.2), 10)
    pygame.draw.rect(window,GOLD,((display_width-30,0), (30, display_height/1.2)))
    pygame.draw.line(window, BLUE, (0, display_height/1.2), (display_width, display_height/1.2), 4)
    window.blit(word,(x,y))

# fn that shows user input
def show_input(events):
    textbox.set_pos(display_width / 2.95, display_height / 1.09)
    textbox.update(events)
    pygame.draw.rect(window, WHITE, ((display_width/3, display_height / 1.1), (display_width/3, 35))) # input box!!
    pygame.draw.line(window,SALMON,(display_width/3, display_height / 1.1),(display_width/3,(display_height/1.1)+35),7)
    pygame.draw.line(window, SALMON, ((display_width / 3)*2, display_height / 1.1),((display_width / 3)*2, (display_height / 1.1) + 35), 7)
    pygame.draw.line(window,SALMON,(display_width/3,(display_height/1.1)+35),((display_width / 3)*2,(display_height/1.1)+35),3)
    textbox.draw(window)
    pygame.display.flip()

#text editor that gives white color
def text_score(text,font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

#makes a box that shows the level given to the screen
def show_level(level):
    text = pygame.font.SysFont("Comic Sans Ms", 20)
    sur, rec = text_objects("Level= "+str(level), text)
    rec.center = (100, 40)
    window.blit(sur,rec)
    pygame.display.update()

#Makes a score board and displays it
def score_Board(value):
    text=pygame.font.SysFont("Comic Sans Ms", 20)
    sur,rec=text_objects("Score: ",text)
    rec.center=(830,40)
    window.blit(sur,rec)
    pygame.draw.rect(window,(255,255,255),((865,28),(70,30)),2)
    score=pygame.font.SysFont("Arial,20",20)
    sur1,rec1=text_score(str(value),score)
    rec1.center=(900,910)
    window.blit(sur1,rec1)

#method that returns the dropping points for each level
def setDifficulty(level):
    if level==1:
        return 10
    elif level==2:
        return 20
    elif level==3:
        return 30
    elif level==4:
        return 40
    elif level==5:
        return 50
    else:
        return 60

#sets levels according to the score
def set_level(current_score):
    if current_score<20:
        level=1
    elif current_score>=20 and current_score<50:
        level=2
    elif current_score>=50 and current_score<100:
        level=3
    elif current_score>=100 and current_score<150:
        level=4
    elif current_score>=150 and current_score<200:
        level=5
    else:
        level="max"
    return level

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

    word_width = random.randint(50, display_width//1.11)
    rand=word_width
    current_score=0
    word = return_word()
    text_surface = font.render(word, False, WHITE)

    # loop
    while crashed == False:
        events = pygame.event.get()
        word_display(text_surface, word_width, word_height)
        score_Board(1)
        show_level(1)
        show_input(events)
        for event in events:
            # window exiting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # window min/max effect
            if event.type==pygame.VIDEORESIZE:
                display_width, display_height = event.w, event.h
                pygame.display.set_mode((display_width,display_height),pygame.RESIZABLE)
                if(display_width>w):
                    word_width=(display_width/w)*word_width
                else:
                    word_width=rand
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

                            word_width = random.randint(50, display_width//1.05)
                            input_word = ""
                            word_height = 0
                            continue

        # update window

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
