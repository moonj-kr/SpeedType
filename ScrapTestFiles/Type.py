import pygame
import time
import random
import timeit

pygame.init()

lst = []
display_width = 800
display_heght = 800


gameDisplay =pygame.display.set_mode((display_heght,display_width))
pygame.display.set_caption('Type the Hell Outta Me')
clock =pygame.time.Clock()


#readfile
def readfile(fileName):
    file = open(fileName, encoding="utf-8")
    line = file.readline().strip()
    while line != "":
        lst.append(line)
        line=file.readline().strip()

#text editor that gives black color
def text_objects(text,font):
    textSurface=font.render(text,True,(255,255,255))
    return textSurface,textSurface.get_rect()

#text editor that gives white color
def text_score(text,font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

#returns a word from the list
def returnWord():
    return lst.pop(random.randint(0,len(lst)))

#makes a box that shows the values given to the screen
def show_input(value):
    pygame.draw.rect(gameDisplay, (255, 255, 255), ((100, 735), (250, 30)))
    text = pygame.font.SysFont("Times New Roman", 20)
    sur, rec = text_score(value, text)
    gameDisplay.blit(sur, (120,740))
    pygame.display.update()

#makes a box that shows the level given to the screen
def show_level(level):
    text = pygame.font.SysFont("Times New Roman", 20)
    sur, rec = text_objects("Level= "+str(level), text)
    rec.center = (500, 750)
    gameDisplay.blit(sur,rec)
    pygame.display.update()

#Makes a score board and displays it
def score_Board(value):
    text=pygame.font.SysFont("Comic Sans Ms", 20)
    sur,rec=text_objects("Score: ",text)
    rec.center=(650,750)
    gameDisplay.blit(sur,rec)
    pygame.draw.rect(gameDisplay,(255,255,255),((700,735),(70,30)))
    score=pygame.font.SysFont("Arial,20",20)
    sur1,rec1=text_score(str(value),score)
    rec1.center=(735,748)
    gameDisplay.blit(sur1,rec1)

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




#main method for the display and dropdown or words
def display(text, current_score,level):
    dtext=pygame.font.Font("freesansbold.ttf",20)
    TextSurf, TextRect= text_objects(text,dtext)
    x=random.randint(50,700)
    y=20
    input_word=""
    pygame.display.update()
    a=timeit.default_timer()
    b=timeit.default_timer()
    print(a)
    while y<display_heght-100:
        gameDisplay.fill((0, 0, 0), TextRect)
        pygame.display.update(TextRect)
        show_input(input_word)
        show_level(level)
        score_Board(current_score)
        TextRect.center = (x, y)
        gameDisplay.blit(TextSurf, TextRect)
        # /pygame.draw.line(gameDisplay, (0, 0, 255), (0, 700), (800, 700), 4)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    input_word += event.unicode
                    show_input(input_word)
                elif event.key == pygame.K_BACKSPACE:
                    input_word = input_word[:-1]
                    show_input(input_word)
                if(event.key==pygame.K_RETURN):
                    if input_word!= text:
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
                            gameDisplay.fill((0, 0, 0), TextRect)
                            return current_score
        add_value = setDifficulty(level)
        y=y+add_value
        time.sleep(1)
        clock.tick(120)


#main fun
if __name__ == '__main__':
    current_score=0
    level=1
    crashed = False
    readfile("Wordlist.txt")
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
        word = returnWord()
        pygame.draw.line(gameDisplay, (0, 0, 255), (0, 700), (800, 700), 4)
        current_score=display(word, current_score,level)

        if current_score==None:
            pygame.quit()
            quit()
        if level!=set_level(current_score):
            pygame.draw.rect(gameDisplay,(0,0,0),((450, 730), (100,30)))
            level=set_level(current_score)
        pygame.display.update()
    pygame.quit()