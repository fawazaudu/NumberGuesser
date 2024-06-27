
from random import randint

EASY_ATTEMPTS=10
HARD_ATTEMPTS=5

def check_answer(guess, number):
    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else: print("Congratulations! You guessed correctly")

def choose_difficulty():
    choice = input("Choose a difficulty 'easy' or hard':")
    if choice.lower() == "easy":
        return EASY_ATTEMPTS
    elif choice.lower() == "hard":
        return HARD_ATTEMPTS

print("Welcome to the Number Guessing Game""\nI am thinking of a number between 1 and 100""\nWhat is the number?")
number=randint(1,100)


attempts=choose_difficulty()
print(f"You have {attempts} attempts to guess the number")

guess= int(input("Guess the number:"))
check_answer(guess, number)