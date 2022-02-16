from art import SilentAuctionLogo
#prints logo
print(SilentAuctionLogo)
print("Welcome to the silent auction!")
auction_present = True
bidders = {}
max_bid = 0
max_bidder = ""

#function that adds the bidders to the bidders dictionary
def add_bidder(name, bid):
    bidders[name] = bid

"""
While the auction is commencing, the code below will prompt 
the current user for their name and their bid.  At the end, the 
program will find the highest bid and return it along with the 
name of the highest bidder.
"""
while auction_present:
    name = input("What is your name?\n")
    bid = float(input("What is your bid?\n$"))
    add_bidder(name, bid)
    progress = input("Are there any more bidders present? (Y/N)\n").upper()
    if progress == "N":
        auction_present = False

# sorts the bidders
for key in bidders:
    if bidders[key] > max_bid:
        max_bid = bidders[key]
        max_bidder = key

print(f"The auction has finished and {max_bidder} is the winner"
      f" with a bid of {max_bid}. Congratulations {max_bidder}.")


