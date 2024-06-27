
from random import randint

EASY_ATTEMPTS=10
HARD_ATTEMPTS=5

def check_answer(guess, number, attempts):
    if guess > number:
        print("Your guess is too high")
        return attempts-1
    elif guess < number:
        print("Your guess is too low")
        return attempts-1

    else: print("Congratulations! You guessed correctly")

def choose_difficulty():
    choice = input("Choose a difficulty 'easy' or hard':")
    if choice.lower() == "easy":
        return EASY_ATTEMPTS
    elif choice.lower() == "hard":
        return HARD_ATTEMPTS

def play_game():
 print("Welcome to the Number Guessing Game""\nI am thinking of a number between 1 and 100""\nWhat is the number?")
 number=randint(1,100)


 attempts=choose_difficulty()


 guess=0
 while guess != number:
     print(f"You have {attempts} attempts to guess the number")
     guess= int(input("Guess the number:"))
     attempts=check_answer(guess, number, attempts)

     if attempts==0:
         print("Sorry, you ran out of guesses")
         return



play_game()