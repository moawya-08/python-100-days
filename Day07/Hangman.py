import random
from hangman_words import word_list
from hangman_art import stage 
from hangman_art import logo

word = random.choice(word_list)
display = ""
print(logo)
correct = []
incorrect =[]
lives = 6


for letter in word:
    print("_",end="")

game_over = False
 
while not game_over:

    guess = input("\nGuess a letter: ").lower()
    display =""

    if guess in incorrect or guess in correct:
            print(f"You've already guessed '{guess}'")
    elif guess not in word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life")
        incorrect.append(guess)
        lives -=1
    print(f"***********************{lives}/6 Lives Left**********************")
    print(stage[lives]) 
    
    for letter in word:
        if guess == letter:
            display = display + guess
            correct.append(guess)
        elif letter in correct: 
            display = display + letter
        else :
            display = display + "_"
            
    print("Word to guess:",display) 
    
    if "_" not in display:
        game_over=True
        print("\n************You Win***********")

    elif lives == 0:
        game_over=True
        print("\n***********You Lose***********")
        print(f"\nThe word was: {word}")\

