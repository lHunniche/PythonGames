import pygame, random
pygame.init()
pygame.display.set_caption("Snake_Lasse")
gameWidth = 500
gameHeight = 500
win = pygame.display.set_mode((gameWidth, gameHeight))


run = True

# player variables

playerWidth = 50
playerHeight = 50
playerColor = (0, 255, 0)
velocity = 50
playerSquares = []
playerSquares.append((100, 200, playerWidth, playerHeight))
playerLenght = 1

# food variables
foodX = random.randint(1, 10) * 50
foodY = random.randint(1, 10) * 50
foodWidth = 50
foodHeight = 50
foodColor = (255, 0, 0)
foodVelocity = 0


movingLeft = movingUp = movingDown = movingRight = False
movingRight = True

waitMoveCounter = 0


def drawScene():
    drawPlayer()
    pygame.draw.rect(win, foodColor, (foodX, foodY, foodWidth, foodHeight))
    pygame.display.update()
    win.fill((0, 0, 0))


def drawPlayer():
    for i in range(len(playerSquares)):
        pygame.draw.rect(win, playerColor, playerSquares[i])

def checkIfPlayerExceedMapLimits():
    global playerSquares

    x,y,w,h = playerSquares[0]

    if x < 0:
        x = gameWidth - playerWidth

    if x == gameWidth:
        x = 0

    if y < 0:
        y = gameHeight - playerHeight

    if y == gameHeight:
        y = 0

    playerSquares[0] = x,y,w,h

def checkCollisionWithFood():
    x,y,w,h = playerSquares[0]
    if foodX == x and foodY == y:
        return True
    return False

def checkCollisionWithSelf():
    if len(playerSquares) != len(set(playerSquares)):
        return True
    return False

def startGameOver():
    global playerSquares, playerLenght, foodX, foodY

    playerSquares = []
    playerSquares.append((100, 200, playerWidth, playerHeight))
    playerLenght = 1

    foodX = random.randint(1, 9) * 50
    foodY = random.randint(1, 9) * 50



def handleCollisionWithFood():
    global foodX, foodY, playerLenght

    playerLenght += 1

    x,y,w,h = playerSquares[0]

    tryAgain = True
    while tryAgain:
        foodX = random.randint(0, 9) * 50
        foodY = random.randint(0, 9) * 50

        xDiff = abs(foodX-x)
        yDiff = abs(foodY-y)

        if xDiff+yDiff > 100:
            tryAgain = False



def handleKeyDown(event):
    global movingLeft, movingRight, movingUp, movingDown

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a] and not movingRight:
        movingLeft = True
        movingDown = movingUp = movingRight = False

    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and not movingLeft:
        movingRight = True
        movingDown = movingUp = movingLeft = False

    if keys[pygame.K_UP] or keys[pygame.K_w] and not movingDown:
        movingUp = True
        movingLeft = movingRight = movingDown = False

    if keys[pygame.K_DOWN] or keys[pygame.K_s] and not movingUp:
        movingDown = True
        movingLeft = movingRight = movingUp = False


def movePlayer():
    global playerSquares

    if movingLeft:
        a,b,c,d = playerSquares[0]
        a-= velocity
        playerSquares.insert(0, (a,b,c,d))
        del playerSquares[playerLenght : len(playerSquares)]

    if movingRight:
        a, b, c, d = playerSquares[0]
        a += velocity
        playerSquares.insert(0, (a, b, c, d))
        del playerSquares[playerLenght : len(playerSquares)]

    if movingUp:
        a, b, c, d = playerSquares[0]
        b -= velocity
        playerSquares.insert(0, (a, b, c, d))
        del playerSquares[playerLenght : len(playerSquares)]

    if movingDown:
        a, b, c, d = playerSquares[0]
        b += velocity
        playerSquares.insert(0, (a, b, c, d))
        del playerSquares[playerLenght : len(playerSquares)]


# main loop
while run:

    pygame.time.delay(5) # from 200 to 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            handleKeyDown(event)

    if waitMoveCounter == 30:
        waitMoveCounter = 0
        movePlayer()
        checkIfPlayerExceedMapLimits()

        if checkCollisionWithFood():
            handleCollisionWithFood()
        if checkCollisionWithSelf():
            startGameOver()

    else:
        waitMoveCounter += 1


    drawScene()


pygame.quit()







