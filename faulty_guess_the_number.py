# Faulty Guess the Number Game

import rando

def guess_number():
    print("Welcom to the Guess Game!!")
    number = rando.randint(1,10)
    tries = 0

    while True:
        tries += 1
        guess = input("Enter a number between 1 to 10: ")
        if guess == 'exit':
            print("You lose!")
            break
        if guess > number:
            print("To High, try agan")
        elif guess < number:
            print("Too low, try agin")
        else:
            print("Congrats you win in " + tries + " trys")
            break
        if tries > 5:
            print("You Lose! Too many attemps.")
            break

guess_number
