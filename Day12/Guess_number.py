import random
import art
num = random.randrange(1,101)

def high_or_low(guessed_num):
    if guessed_num > num:
        print("Too high")
    elif guessed_num < num:
        print("Too low")
      
def game():
    guess = 0
    difficulty = input("Choose Difficulty . Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = 10
    else:
        attempts = 5
    while guess != num and attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        high_or_low(guess)
    if guess == num:
        print(f"You got it! The answer was {num}")
    else:
        print(f"You've run out of guesses. The number was {num}")
print(art.logo)   
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
game()

        