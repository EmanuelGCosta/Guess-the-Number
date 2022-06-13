from art import logo
import random


def guess_game(attempts):
    random_num = random.randint(0, 100)
    print(f"The num is {random_num}")
    for attempt in range(0, attempts):
        print(f"You have {attempts - attempt} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_num:
            print("Too high.")
        elif guess < random_num:
            print("Too low.")
        elif guess == random_num:
            return f"You got it! The answer was {random_num}."

    return "You've run out of guesses, you lose"


def play_game():
    hard = 5
    easy = 10

    print(logo)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose == "easy":
        print(guess_game(easy))
    elif choose == "hard":
        print(guess_game(hard))


play_game()
play_again = True

while play_again:
    play = input("Want's to play again? Type 'yes' or 'no'.").lower()
    if play == "yes":
        play_game()
    elif play == "no":
        play_again = False
    else:
        print("Enter a valid Keyword")

