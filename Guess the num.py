import random

randomNum = random.randint(1,100)
while True:
    print("to play press (P) or to Quit (Q) ")
    userInput = input().lower()
    if userInput == 'p':
        while True:
                new_userInput = int(input())
                if new_userInput == randomNum:
                    print("yo you guess the currect num!\nwanna play again?")
                    break
                elif new_userInput < randomNum:
                    print("the number is too low\ntry again")
                elif new_userInput > randomNum:
                    print("the number is too high\ntry again")


    elif userInput == 'q':
        print("__Game Over__")
        break
















