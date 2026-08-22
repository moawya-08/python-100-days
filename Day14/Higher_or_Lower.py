import random
import art
import game_data

def print_score():
    if Score !=0:
        print(f"Correct, You'r Current Score: {Score}")
    
correct_answer = ""        
Score = 0
options = random.sample(game_data.data,k=2)
game_over =True


option_A = options[0]
option_A_name = (option_A["name"])
option_A_followers =(option_A["follower_count"])
option_A_description = (option_A["description"])
option_A_country = (option_A["country"])

option_B = options[1]
option_B_name = (option_B["name"])
option_B_followers =(option_B["follower_count"])
option_B_description = (option_B["description"])
option_B_country = (option_B["country"])

while game_over:
    print(art.logo)
    print_score()
    print(f"Compare A: {option_A_name}, a {option_A_description}, from {option_A_country}")
    print(art.vs)
    print(f"Against B: {option_B_name}, a {option_B_description}, from {option_B_country}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if option_A_followers > option_B_followers:
        correct_answer = "a"
    else:
        correct_answer = "b"
    
    if correct_answer == choice:
        Score += 1
        option_A_country = option_B_country
        option_A_description =option_B_description
        option_A_followers = option_B_followers
        option_A_name = option_B_name
        option_B = random.choice(game_data.data)
        option_B_name = (option_B["name"])
        option_B_followers =(option_B["follower_count"])
        option_B_description = (option_B["description"])
        option_B_country = (option_B["country"])
        print("\n"*20)
    else:
        print("\n"*20)
        print(f"Sorry thats Wrong,.Final Score: {Score}")
        game_over = False

