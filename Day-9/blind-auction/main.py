from replit import clear
#HINT: You can call clear() to clear the output in the console.
def add_new_bidder(name,bid):
  new_dict = {}
  new_dict["name"] = name
  new_dict["bid"] = bid

  bidders.append(new_dict)

bidders=[]

def highest_bidder(bidders):
  highest_bid = 0
  highest_bidder = ""
  for bidder in bidders:
    if bidder["bid"] > highest_bid:
      highest_bid = bidder["bid"]
      highest_bidder = bidder["name"]      
  print(f"{highest_bidder} has won the auction with bid amount of ${highest_bid}")


while True:
  bidder_name = input("Enter Your Name: ")
  bid_amount = int(input("What's your bid? $"))

  add_new_bidder(bidder_name,bid_amount)

  other_bidder = input("Any other Bidders? Type Yes or No: ").lower()

  if other_bidder == "yes":
    clear()
  elif other_bidder == "no":
    highest_bidder(bidders)
    break
    


  

  
  