import os
from art import logo
# os.system("cls")
print(logo)

bids = {}
bidding_finished =False

def find_highest_bidder(bidding_record):
    highest_bid =0
    for bidder in bidding_record:
        bid_amout = bidding_record[bidder]
        if bid_amout>highest_bid:
            highest_bid = bid_amout
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')

while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid? $"))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'y' for yes or 'n' for no.")
    if should_continue == "n":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue=="y":
        os.system("cls")