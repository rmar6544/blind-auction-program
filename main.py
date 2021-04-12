from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
clear()
print(logo)
bid = True
while bid == True:
  bidders_name = input("what is your name? ")
  bid_amount = input("Enter your bid amount: ")
  bidder_dic = {}
  bidder_dic[bidders_name]= bid_amount
  bidder_dic += 1
  other_bidders = input("Are there other bidders? type 'yes' or 'no'").lower()
  if other_bidders == "yes":
    clear()
  elif other_bidders == "no":
    for key in bidder_dic:
      if bidder_dic[key] > 0:
        print(f"{bidder_dic[key]} is the winning bidder." )
        bid = False
  print(bidder_dic)      