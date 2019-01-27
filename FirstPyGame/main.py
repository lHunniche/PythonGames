import pygame, random, os
from explosion import Explosion
from score import Score
from highscore import Highscore
from backgroundmusic import BackgroundMusic
from wordListMIT import WordListMIT

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
pygame.display.set_caption("TypeMaster")
gameWidth = 1400
gameHeight = 800
spawnWordEvent = 25
moveWordEvent = 26
increaseSpeedEvent = 27

textArea = ""

gameOver = False
level = 1
gameScore = Score(int(gameWidth*0.15), gameHeight-50)
gameHighscore = Highscore(int(gameWidth*0.72), gameHeight-50)

win = pygame.display.set_mode((gameWidth, gameHeight))
font = pygame.font.SysFont("Comic Sans MS", 30)
words = WordListMIT.listOfWords

onScreenExplosions = []
sampleExplosion = Explosion(0, 0)

bgMusic = BackgroundMusic("halo")

wordsInPlay = []

spawnInterval = 2800
movePerMs = 15
pygame.time.set_timer(spawnWordEvent, spawnInterval)
pygame.time.set_timer(moveWordEvent, movePerMs)

pygame.time.set_timer(increaseSpeedEvent, 10000)

# spawn first word immidiately
spawnWordNow = pygame.event.Event(spawnWordEvent, {})
pygame.event.post(spawnWordNow)

run = True


def drawWords():
    for i in range(len(wordsInPlay)):
        textSurface, position, word = wordsInPlay[i]
        win.blit(textSurface, position)

def drawScore():
    textSurface = font.render(gameScore.getScore(), True, gameScore.color)
    position = (gameScore.xCord, gameScore.yCord)

    win.blit(textSurface, position)

def colorHalfwayWordsOrange():
    if len(wordsInPlay) == 0:
        return

    for i in range(len(wordsInPlay)):
        surface, position, word = wordsInPlay[i]
        x, y = position
        if gameWidth//2 > x:
            newSurface = font.render(word, True, (255, 148, 0))
            wordsInPlay[i] = (newSurface, position, word)
        else:
            return

def colorNearlyThereWordsRed():
    if len(wordsInPlay) == 0:
        return

    for i in range(len(wordsInPlay)):
        surface, position, word = wordsInPlay[i]
        x, y = position
        if gameWidth//4 > x:
            newSurface = font.render(word, True, (226, 45, 45))
            wordsInPlay[i] = (newSurface, position, word)
        else:
            return



def drawHighscore():
    if gameScore.score > int(gameHighscore.highscore):
        textSurface = font.render(gameScore.getScoreAsNewHighScore(), True, gameHighscore.color)
        position = (gameHighscore.xCord, gameHighscore.yCord)

        win.blit(textSurface, position)
    else:
        textSurface = font.render(gameHighscore.getHighscore(), True, gameHighscore.color)
        position = (gameHighscore.xCord, gameHighscore.yCord)

        win.blit(textSurface, position)


def spawnWord():
    if gameOver:
        return

    global wordsInPlay

    text = words[random.randint(0, len(words)-1)]
    textSurface = font.render(text, True, (100, 255, 0))

    spawnHeight = 0
    tryAgain = True
    while tryAgain:

        if len(wordsInPlay) == 0:
            spawnHeight = gameHeight//2
            tryAgain = False
        else:
            spawnHeight = random.randint(0, gameHeight-100)

            surface1, position1, text1 = wordsInPlay[max(len(wordsInPlay)-1, 0)]
            surface2, position2, text2 = wordsInPlay[max(len(wordsInPlay)-2, 0)]
            x1, y1 = position1
            x2, y2 = position2

            diff1 = abs(spawnHeight-y1)
            diff2 = abs(spawnHeight-y2)

            if diff1 > 100 and diff2 > 100:
                tryAgain = False

    position = (gameWidth, spawnHeight)

    wordsInPlay.append((textSurface, position, text))


def moveWords():
    global wordsInPlay
    for i in range(len(wordsInPlay)):
        textSurface, position, text = wordsInPlay[i]
        x,y = position
        x -= 1

        position = (x, y)
        wordsInPlay[i] = (textSurface, position, text)


def drawTextArea():
    leftTextBoundsSurface = font.render(">", True, (0, 255, 0))
    rightTextBoundsSurface = font.render("<", True, (0, 255, 0))

    leftTextBoundsPosition = (gameWidth/2-150, gameHeight-50)
    rightTextBoundsPosition = (gameWidth/2+150, gameHeight-50)

    textSurface = font.render(textArea, True, (255, 255, 255))
    textPosition = (gameWidth/2-textSurface.get_rect().width/2+7, gameHeight-50)

    win.blit(leftTextBoundsSurface, leftTextBoundsPosition)
    win.blit(rightTextBoundsSurface, rightTextBoundsPosition)
    win.blit(textSurface, textPosition)


def increaseSpeed():
    if gameOver:
        return

    global spawnInterval, movePerMs

    speedIncreased = False

    if movePerMs > 11:
        movePerMs -= 1
        speedIncreased = True

    if spawnInterval != 1500:
        spawnInterval -= 100
        spawnInterval = int(spawnInterval)
        pygame.time.set_timer(spawnWordEvent, spawnInterval)

        spawnEvent = pygame.event.Event(spawnWordEvent, {})
        pygame.event.post(spawnEvent)
        pygame.time.set_timer(moveWordEvent, movePerMs)

        speedIncreased = True

    if speedIncreased:
        print("Speed increased, now spawns every " + str(spawnInterval) + " ms, and moves every " + str(movePerMs) + " ms...")


def drawExplosion():
    for index, explosion in enumerate(onScreenExplosions):
        if explosion.frameCounter == explosion.totalFrames:
            del onScreenExplosions[index]
        else:
            indexToDraw = explosion.frameCounter//explosion.frames
            x = explosion.xCord - (explosion.explosionImages[indexToDraw].get_rect().width/2)
            y = explosion.yCord - (explosion.explosionImages[indexToDraw].get_rect().height/2)
            explosion.incrementFrameCounter()

            win.blit(explosion.explosionImages[indexToDraw], (x, y))



def handleKeyDown(keyEvent):
    global textArea

    if keyEvent.unicode.isalpha():
        textArea += keyEvent.unicode
    elif keyEvent.key == pygame.K_BACKSPACE:
        textArea = textArea[:-1]
    elif keyEvent.key == pygame.K_RETURN:
        textArea = ""




def checkIfWordIsWritten():
    global wordsInPlay, textArea

    for index, (textSurface, position, word) in enumerate(wordsInPlay):
        if textArea == word:
            x, y = position
            newExplosion = Explosion(x, y)
            onScreenExplosions.append(newExplosion)

            del wordsInPlay[index]
            textArea = ""

            newPoints = 100 + (level-1)*10
            gameScore.score += int(newPoints)

            sampleExplosion.explosionSound.play()


def drawScene():
    global wordsInPlay

    pygame.draw.line(win, (62, 19, 96), (0, gameHeight-50), (gameWidth, gameHeight-50), 2)
    colorHalfwayWordsOrange()
    colorNearlyThereWordsRed()
    drawWords()
    drawExplosion()
    drawTextArea()
    drawScore()
    drawHighscore()
    pygame.display.update()
    win.fill((0, 0, 0))


# main loop
def isGameOver():
    global gameOver, wordsInPlay
    if len(wordsInPlay) == 0:
        return

    surface, position, word = wordsInPlay[0]
    x, y = position
    if x < 0:
        gameOver = True
        gameHighscore.checkForNewHighScore(gameScore.score)
        wordsInPlay = [(font.render("Game Over", True, (255, 255, 255)), (gameWidth // 2 - 50, gameHeight // 2), "Game Over")]
        pygame.time.set_timer(spawnWordEvent, 100000000)



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
        elif event.type == pygame.KEYDOWN:
            handleKeyDown(event)

    checkIfWordIsWritten()

    isGameOver()
    drawScene()


pygame.quit()







