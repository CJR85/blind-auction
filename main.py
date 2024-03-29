# from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bid(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is the {winner} with a bid of £{highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your price?: £"))
  bids[name] = price
  should_continue = input("Are there any othe bidders? Type 'yes' or 'no'.\n")
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bid(bids)
  elif should_continue == 'yes':
    print("\033[2J\033[1;1H")  # Clear the output between guesses