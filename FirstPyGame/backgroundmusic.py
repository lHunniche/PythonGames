import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

class BackgroundMusic:


    def __init__(self, selection):
        self.music = "a"
        if selection == "france":
            pygame.mixer.music.load("assets/backgroundmusic/tourdefrance.mp3")

        elif selection == "halo":
            pygame.mixer.music.load("assets/backgroundmusic/halo.mp3")
        else:
            pygame.mixer.music.load("assets/backgroundmusic/default.mp3")
        pygame.mixer.music.play(-1, 0.0)


