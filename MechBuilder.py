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
    def launchTitleMenu(self):
        print("Welcome to v0.0.0.1 of the game!")
        print("What would you like to do?:")
        print("(N)ew Game, (C)ontinue, e(X)it)")
        s = str(takeInput())
        try:
            while s:
                if s.upper() == 'N' or s.upper() == 'NEW GAME':
                    return 1
                elif s.upper() == 'C' or s.upper() == 'CONTINUE':
                    pass
                elif s.upper() == 'X' or s.upper() == 'EXIT':
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
    def getActionCode(self, action_code):
        __logic_codes = ('title_sequence', 'new_game')
        while action_code:
            return __logic_codes[action_code]
        else:
            return 'title_sequence'

        
class GameManager:
    def __init__(self, code_key={'title_sequence': 0}):
        self.code_key = code_key
    
    # Initiates game, handles main menu placeholder
    def launchTitleMenu(self, startMenu=TitleMenu()):
        startMenu.launchTitleMenu()

    def launchNewGame(self, title_menu_output, new_game_handler):
        new_game_handler.newGame(start_game_output)

    def runSequence(self, sequence_name):
        
        
__logicHandler = LogicHandler()
__gameManager = GameManager()
a = __gameManager.runSequence(__logicHandler.GetAction(0))
while a:
else:
    if a == 0:
        a = __gameManager.runSequence(__logicHandler.GetAction(0))
    else:
        quit()
