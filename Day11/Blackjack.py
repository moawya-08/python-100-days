import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# print("Computer cards: ",computer_hand,"\n\n")


def ace(_hand):
    while 11 in _hand and sum(_hand) > 21:
        position = _hand.index(11)
        _hand[position] = 1
 
play =True            
while play:
    play = input("\nDo you want to play game of Blackjack? 'y' or 'n': ").lower()
    
    if play == "y":
        user_hand = random.choices(cards,k=2)
        computer_hand = random.choices(cards,k=2)
        print(logo)
        user_score =sum(user_hand)
        computer_score = sum(computer_hand)
        
        
        game_end = True
        if computer_hand == [10,11] or computer_hand == [11,10]:
                print("COMPUTER GOT BLACKJACK")
                print("***********YOU LOSE***********")
                game_end = False
        elif user_hand == [10,11] or user_hand == [11,10]:
                print("YOU GOT BLACKJACK")
                print("***********YOU WIN***********")
                game_end = False 
            
        while game_end:
            
                
            user_score =sum(user_hand)
            computer_score = sum(computer_hand)       
            print("\nYour cards: ",user_hand, "Current Score: ",sum(user_hand))
            print("Coumputers first card: ",computer_hand[0])
            another_card = input("Do you want another card 'y' or pass 'n': ").lower()
            
            if another_card == "n":
                
                while sum(computer_hand) <= 16:
                    computer_hand.append(random.choice(cards))
                    ace(computer_hand)
                if sum(computer_hand) > 21:
                    print("Game Over Computer Went Above 21")
                    print("***********YOU WIN**************")
                    game_end = False
                elif sum(computer_hand) < sum(user_hand):
                    print("***********YOU WIN**************")
                    game_end = False
                elif sum(computer_hand) == sum(user_hand):
                    print("**************Draw**************")
                    game_end = False
                elif sum(computer_hand) > sum(user_hand): 
                    print("you lose")  
                    game_end = False
            if another_card == "y":
                user_hand.append(random.choice(cards))
                ace(user_hand)
                if sum(user_hand) > 21:
                    print("You went over 21. You lose ")
                    print("**********YOU LOSE************")
                    game_end = False
                
        print("\n   Your final hand:   ",user_hand, ",Final score:",sum(user_hand))
        print("Computers final hand: ",computer_hand, "  ,Final score:",sum(computer_hand))  
                
    else:
        print("WHAAAAAAAAAAAT")