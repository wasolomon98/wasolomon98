from NewGame import NewGame
from TitleMenu import TitleMenu

class GameManager:
    def runSequence(self, sequence_name):
        code_key={'title_sequence': 0, 'new_game': 1}
        if code_key[sequence_name] == 0:
            o = TitleMenu.launchTitleMenu()
            return o
        elif code_key[sequence_name] == 1:
            o = NewGame.newGame()
            return o
