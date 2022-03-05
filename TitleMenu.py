import GameFunctions

class TitleMenu:
    def launchTitleMenu():
        print("Welcome to v0.0.0.1 of the game!")
        print("What would you like to do?:")
        print("(N)ew Game, (C)ontinue, e(X)it)")
        s = GameFunctions.takeStrInput()
        while s:
            if s.upper() == 'N' or s.upper() == 'NEW GAME':
                return 1
            elif s.upper() == 'C' or s.upper() == 'CONTINUE':
                pass
            elif s.upper() == 'X' or s.upper() == 'EXIT':
                quit()
            else:
                print("I didn't understand that.")
                s = GameFunctions.takeStrInput()
