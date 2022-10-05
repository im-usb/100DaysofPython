#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

EASY_CHANCES = 10
HARD_CHANCES = 5

import random
import art


def guess(guess_no, actual_no):
    difference = abs(guess_no - actual_number)

    if guess_no > actual_no and difference < 10:
        return "You're Getting Close"
    elif guess_no > actual_no:
        return "Too High"
    elif guess_no < actual_no and difference < 10:
        return "You're Getting Close"
    elif guess_no < actual_no:
        return "Too low"
    elif guess_no == actual_no:
        return "Congrats You Got It Right!!"

game_play = 'y'

while game_play == 'y':
    print(art.logo)
    print('WELCOME TO THE GAME OF NUMBER GUESSING')
    level = input(
        "WHAT LEVEL OF DIFFICULTY WOULD YOU PREFER? TYPE easy OR hard?: "
    ).lower()
    actual_number = random.randint(1, 100)

    if level == 'easy':
        chances = EASY_CHANCES

        while chances > 0:
            print(f"YOU HAVE {chances} CHANCES")
            guess_number = int(input("TAKE A GUESS: "))
            result = guess(guess_number, actual_number)
            print(result)
            chances -= 1

            if guess_number == actual_number:
                chances = 0
    elif level == 'hard':
        chances = HARD_CHANCES

        while chances > 0:
            print(f"YOU HAVE {chances} CHANCES")
            guess_number = int(input("TAKE A GUESS: "))
            result = guess(guess_number, actual_number)
            print(result)
            chances -= 1

            if guess_number == actual_number:
                chances = 0
    print(f"THE ACTUAL NUMBER WAS {actual_number}")
    game_play = input("DO YOU WANT TO PLAY AGAIN? Y or N: ").lower()
