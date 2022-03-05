from LogicHandler import LogicHandler
from GameManager import GameManager

logicHandler = LogicHandler()
gameManager = GameManager()

x = logicHandler.getActionCode(0)
while True:
    while True:
        x = gameManager.runSequence(x)
        x = logicHandler.getActionCode(x)
    else:
        quit()
