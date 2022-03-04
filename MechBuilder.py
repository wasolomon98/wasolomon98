def takeInput(self):
    s = str(input('> '))
    return s

class Pilot:
    def __init__(self, name, attributes={}, skills=[], inventory=[]):
        self.name = name
        self.rank = "Cadet"
        self.attributes = attributes
        self.skills = skills
        self.inventory = inventory


class Mech:
    def __init__(self, name, __serial_number='', tier=0):
        self.name = name
        self.__serial_number = __serial_number
        self.tier = tier

class StartMenu:
    def titleMenu(self):
        print("Welcome to v0.0.0.1 of the game!")
        print("What would you like to do?:")
        print("(N)ew Game, (C)ontinue, e(X)it)")
        s = str(takeInput())
        try:
            while s:
                if s.upper() == 'N':
                    return 0
                elif s.upper() == 'C':
                    pass
                elif s.upper() == 'X':
                    quit()
                else:
                    print("I didn't understand that.")
                    s = str(takeInput())
        except:
            print('INVALID ENTRY AT STARTGAME')

class NewGameHandler:
    def newGame(a):
        print("YOU HAVE CHOSEN TO FOUND A NEW COMPANY")
        print("How many pilots do you have?:")
        s = str(self.takeInput())
        t = True
        while t:
            while s:
                if s = 1
            else:
                if s < 0:
                    print('You cannot have a negative number of pilots!')
                    print("How many pilots do you have?:")
                    s = str(self.takeInput())  
                else: 
                    print('You must have at least 1 pilot!')
                    print("How many pilots do you have?:")
                    s = str(self.takeInput())    

# Controls the GameManager through a series of automated codes.
# Makes it easier to jump between different scenes/functions by automating transitions.
class LogicHandler:
    # Main 
    def getAction(self, action_code):
        pass
        


class GameManager:
    # Initiates game, handles main menu placeholder
    def launchTitleMenu(self, start_menu_handler)

    def launchNewGame(self, title_menu_output, new_game_handler):
        new_game_handler.newGame(start_game_output)


__gameManager = GameManager()
__startMenu = StartMenu()
__gameManager.startGame(__startMenu)
a = __gameManager.startGame()
