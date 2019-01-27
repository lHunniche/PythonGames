class Highscore:

    xCord = None
    yCord = None
    highscore = None
    color = (255, 255, 0)
    highscoreFile = None

    def __init__(self, x, y):
        self.xCord = x
        self.yCord = y
        self.highscoreFile = open("highscore.txt", "r")
        self.highscore = self.highscoreFile.read()

    def getHighscore(self):
        return "Highscore: " + str(self.highscore)

    def checkForNewHighScore(self, score):
        if int(score) > int(self.highscore):
            self.highscoreFile = open("highscore.txt", "w")
            self.highscoreFile.write(str(score))


