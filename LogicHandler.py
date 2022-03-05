class LogicHandler:
    def getActionCode(self, action_code):
        __logic_codes = (None, 'new_game')
        while action_code:
            return __logic_codes[action_code]
        else:
            return 'title_sequence'


