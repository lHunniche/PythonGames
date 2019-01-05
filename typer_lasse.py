import pygame, random, os
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Typer_Lasse")
gameWidth = 1400
gameHeight = 800
spawnWordEvent = 25
moveWordEvent = 26
increaseSpeedEvent = 27

win = pygame.display.set_mode((gameWidth, gameHeight))
font = pygame.font.SysFont("Comic Sans MS", 30)
words = ["html", "ide", "machine", "program", "ascii", "agile", "algorithm",
         "applet", "array", "boolean", "bug", "tracking", "bean", "compiler",
         "concatenation", "css", "datalog", "decompiler", "developer",
         "django", "dump", "database", "elif", "flat-class-path", "function",
         "hashcode", "hardcode", "hex", "editor", "pascal"]

wordsInPlay = []
pygame.time.set_timer(spawnWordEvent, 5000)
pygame.time.set_timer(moveWordEvent, 50)

pygame.time.set_timer(increaseSpeedEvent, 10000)

# spawn first word immidiately
spawnWordNow = pygame.event.Event(spawnWordEvent, {})
pygame.event.post(spawnWordNow)

run = True


def drawWords():
    for i in range(len(wordsInPlay)):
        textSurface, position = wordsInPlay[i]
        win.blit(textSurface, position)

def spawnWord():
    global wordsInPlay

    textSurface = font.render(words[random.randint(0, len(words)-1)], True, (255,255,255))
    position = (gameWidth, random.randint(0, gameHeight-100))
    wordsInPlay.append((textSurface, position))

def moveWords():
    global wordsInPlay
    for i in range(len(wordsInPlay)):
        textSurface, position = wordsInPlay[i]
        x,y = position
        x -= 1

        position = (x, y)
        wordsInPlay[i] = (textSurface, position)

def increaseSpeed():
    print("")

def handleKeyDown(event):
    if event.unicode.isalpha():
        name += evt.unicode
    elif event.key == K_BACKSPACE:
        name = name[:-1]
    elif event.key == K_RETURN:
        name = ""

def drawScene():
    pygame.draw.line(win, (62, 19, 96), (0, gameHeight-50), (gameWidth, gameHeight-50), 2)
    drawWords()
    pygame.display.update()
    win.fill((0, 0, 0))



# main loop
while run:
    clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == spawnWordEvent:
            spawnWord()
        elif event.type == moveWordEvent:
            moveWords()
        elif event.type == increaseSpeedEvent:
            increaseSpeed()
        elif event.type == KEYDOWN:
            handleKeyDown(event)

    drawScene()


pygame.quit()







