class Score:

    xCord = None
    yCord = None
    score = 0
    color = (255, 255, 0)

    def __init__(self, x, y):
        self.xCord = x
        self.yCord = y

    def getScore(self):
        return "Score: " + str(self.score)

    def getScoreAsNewHighScore(self):
        return "Highscore: " + str(self.score)

