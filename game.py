from playerTurnFunctions import doPlayerOneTurn, doPlayerTwoTurn

userInput = input("Start game? (y/n)\n")

if userInput == 'y':
    for x in range (0,13):
        doPlayerOneTurn()
        #doPlayerTwoTurn()
    print("End of Game")
else:
    print("You didn't want to play.")