import game

set up
    g = game.Game(0,0)

at game start result is zero and zero
    g.result() == (0,0)

when player one wins ball his score is 15
    g.winBallPlayer1()
    g.result() == (15,0)

when player one wins ball twice his score is 30
    g.winBallPlayer1()
    g.winBallPlayer1()
    g.result() == (30,0)

when player two wins ball his score is 15
    g.winBallPlayer2()
    g.result() == (0, 15)

when player one wins ball and player two wins ball score is 15 15
    g.winBallPlayer1()
    g.winBallPlayer2()
    g.result() == (15, 15)

when score is 40 40 game is deuce
    g = game.Game(3,3)
    g.result() == "deuce"

when score is 40 40 and player1 wins ball game is adv 40
    g = game.Game(3,3)
    g.winBallPlayer1()
    g.result() == ("advantage", 40)

when score is advantage 40 and player2 wins ball game is deuce
    g = game.Game(4,3)
    g.winBallPlayer2()
    g.result() == "deuce"

when score is 40 advantage and player1 wins ball game is deuce
    g = game.Game(3,4)
    g.winBallPlayer1()
    g.result() == "deuce"

when score is adv 40 and player1 wins ball player 1 wins
    g = game.Game(4,3)
    g.winBallPlayer1()
    g.result() == ("win", 40)

when score is 40 adv and player2 wins ball player 2 wins
    g = game.Game(3,4)
    g.winBallPlayer2()
    g.result() == (40, "win")

when score is 40 30 and player1 wins ball player 1 wins
    g = game.Game(3,2)
    g.winBallPlayer1()
    g.result() == ("win", 30)

when score is 15 40 and player2 wins ball player 2 wins
    g = game.Game(1,3)
    g.winBallPlayer2()
    g.result() == (15, "win")

when win1 win2 win1 win2 win1 win2 win1 game is adv 40 and when player2 wins game is deuce and when player2 wins two times player2 wins
    g.winBallPlayer1()
    g.winBallPlayer2()
    
    g.winBallPlayer1()
    g.winBallPlayer2()

    g.winBallPlayer1()
    g.winBallPlayer2()

    g.winBallPlayer1()

    g.result() == ("advantage",40)

    g.winBallPlayer2()

    g.result() == "deuce"

    g.winBallPlayer2()
    g.winBallPlayer2()

    g.result() == (40, "win")
