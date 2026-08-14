from art import logo
print(logo)

def find_highest_bid(bidding_record):
    winner = ""
    highest_bid = 0
    for name, bid in auction.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = name

    return winner, highest_bid

other = True
auction ={}
while other:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    other = input("Are the any other biddiers? Type 'yes' or 'no'\n")
    auction[name] = bid
    winner, highest_bid = find_highest_bid(auction)
    
        
    if other == "no":
        other = False
        print(f"The winner is {winner} with a bid of {highest_bid}")
    else:
        print("\n"*100)