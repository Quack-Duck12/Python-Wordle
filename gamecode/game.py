from utils import *

class game():

    def __init__(self) -> None:
        
        self.answer: str = LoadWord()
        self.attemps: int = 6

    def GameLoop(self):

        self.Initilize()

    def Initilize(self) -> None:

        print("\n\n")
        print("*" * 20)
        print("Welocome To Wordle")
        print("*" * 20)
        print("Game Rules: ' _ ' = Unguessed, ' * ' = Within Word")
        print("*" * 20)
        print("_ " * 5)

    def  Input(self) -> None:

        word = ""
        while len(word) != 5:
            word = str(input(f"Enter Your Guess(5 Letters): "))

    def CheckGuess(self) -> None:
        

game().GameLoop()
