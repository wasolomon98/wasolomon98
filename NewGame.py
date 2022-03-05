import GameFunctions
import Pilot

class NewGame:
    def newGame():
        print("YOU HAVE CHOSEN TO FOUND A NEW COMPANY")
        print("How many pilots do you have? (MAX 4):")
        i = GameFunctions.takeIntInput()
        t = True
        while t:
            if i:
                if i < 0:
                    print('You cannot have a negative number of pilots!\n')
                    print("How many pilots do you have?:")
                    i = GameFunctions.takeIntInput()
                elif i == 1:
                    print('You have selected a single pilot')
                    print('SUCCESS')
                    break
                elif 1 < i < 5:
                    print('You have selected ' + str(i) + ' pilots')
                    print('SUCCESS')
                    break                    
                else:
                    print('You can only have up to 4 pilots!\n')
                    i = GameFunctions.takeIntInput()
            else:
                print('You must have at least 1 pilot!\n')
                print("How many pilots do you have?:")
                i = GameFunctions.takeIntInput()
