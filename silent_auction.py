from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bids = {}
bidding_finished = False

def find_winner(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there more bidders? 'Y' for yes, 'N' for no: ").lower()
  if should_continue == 'n' or should_continue == "no":
    clear()
    bidding_finished = True
    find_winner(bids)
  elif should_continue == 'y' or should_continue == 'yes':
    clear()
