import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

class Explosion:
    xCord = None
    yCord = None
    window = None
    explosionImages = [pygame.image.load("assets/explosion/regularExplosion00.png"), pygame.image.load("assets/explosion/regularExplosion01.png"), pygame.image.load("assets/explosion/regularExplosion02.png"),
                       pygame.image.load("assets/explosion/regularExplosion03.png"), pygame.image.load("assets/explosion/regularExplosion04.png"), pygame.image.load("assets/explosion/regularExplosion05.png"),
                       pygame.image.load("assets/explosion/regularExplosion06.png"), pygame.image.load("assets/explosion/regularExplosion07.png"), pygame.image.load("assets/explosion/regularExplosion08.png")]
    frameCounter = 0
    frames = len(explosionImages)
    totalFrames = frames * 2
    explosionSound = pygame.mixer.Sound("assets/explosion/explosionSound.wav")

    def __init__(self, x, y):
        self.xCord = x
        self.yCord = y

    def incrementFrameCounter(self):
        self.frameCounter += 1
