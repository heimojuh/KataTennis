class Game:

    scores = (0, 15, 30, 40, "advantage", "win")
    
    def __init__(self, score1, score2):
        self.player1 = [score1]
        self.player2 = [score2]

    def run(self):
        pass
    
    def result(self):
        if self.player1[0] == 3 and self.player2[0] == 3:
            return "deuce"
        return (self.scores[self.player1[0]],self.scores[self.player2[0]])

    def winBallPlayer1(self):
        adv = self.checkAdvantageAndWinBall(self.player1, self.player2)
        if adv:
            return

        self.player1[0] = self.player1[0] + 1

    def winBallPlayer2(self):
        adv = self.checkAdvantageAndWinBall(self.player2, self.player1)
        if adv:
            return
        
        self.player2[0] = self.player2[0] + 1

    def checkAdvantageAndWinBall(self, playerWinning, playerLosing):
        if playerLosing[0] == 4:
            playerLosing[0] = 3
            return True
        if playerWinning[0] == 3 and playerLosing[0] < 3:
            playerWinning[0] = 5
            return True
        return False
