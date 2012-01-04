class Game:

    scores = (0, 15, 30, 40, "advantage", "win")
    player1 = 0;
    player2 = 0;
    
    def run(self):
        pass
    
    def result(self):
        if self.player1 == 3 and self.player2 == 3:
            return "deuce"
        return (self.scores[self.player1],self.scores[self.player2])

    def winBallPlayer1(self):
        adv = self.checkAdvantageAndWinBall(self.player1, self.player2)
        if adv:
            self.player1 = adv[0]
            self.player2 = adv[1]
            return

        self.player1 = self.player1 + 1

    def winBallPlayer2(self):
        adv = self.checkAdvantageAndWinBall(self.player2, self.player1)
        if adv:
            self.player2 = adv[0]
            self.player1 = adv[1]
            return
        
        self.player2 = self.player2 + 1

    def checkAdvantageAndWinBall(self, playerWinning, playerLosing):
        if playerLosing == 4:
            res = (playerWinning, playerLosing-1)
            return res
        return False
