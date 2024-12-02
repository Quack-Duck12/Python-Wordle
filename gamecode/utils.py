def LoadWord() -> str:
    from random import choice

    with open("gamecode\Word_List.txt", 'r') as file:
        words = eval(file.read())

        return choice(words)