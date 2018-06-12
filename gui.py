import pygame

pygame.font.init()

lst = []
display_width = 800
display_height = 600
word_height = 0

black = (0,0,0)
white = (255, 255, 255)

# fn to read file of words
def readfile():
    file = open("Wordlist.txt", "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        lst.append(line.strip())

# helper fn to return word
def returnWord():
    readfile()
    return lst.pop()

# window setup
font = pygame.font.SysFont("Veranda", 30)
text_surface = font.render(returnWord(), False, white)

window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Speed Type")
clock = pygame.time.Clock()
crashed = False

# displaying words
def word_display(word,x,y):
    window.fill(black)
    window.blit(word,(x,y))

def popup():
    print("You ran out of time!")
    window.fill(white)

# word location stuff
while crashed == False:
    for event in pygame.event.get():
        # window exiting
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    # word display
    word_display(text_surface,display_width/2,word_height)

    # update window
    pygame.display.update()
    word_height += 50

    # border
    if word_height > 500:
        popup()
        crashed = True

    # fps
    clock.tick(2)
pygame.quit()