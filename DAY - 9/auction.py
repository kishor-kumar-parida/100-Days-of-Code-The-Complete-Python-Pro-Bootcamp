import os
from art import logo


def clear():
    os.system("cls" if os.name == "nt" else "clear")


print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bids):
    max_bid = 0
    bidder_name = ""
    for bidder in bids:
        if bids[bidder] >= max_bid:
            max_bid = bids[bidder]
            bidder_name = bidder

    print(f"Winner is {bidder_name} and Bid value is {max_bid}")


while not bidding_finished:
    name = input("Your Name: ")
    price = int(input("Price: "))

    bids[name] = price

    should_countinue = input("Any other bidders type 'yes' or 'no'?: ").lower()

    if should_countinue == "no":
        bidding_finished = True
        find_highest_bidder(bids)

    elif should_countinue == "yes":
        clear()

    else:
        print("Please enter correct operation")
