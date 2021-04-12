#imports
from replit import clear
from art import logo

#create an empty dictionary
bidder_dic = {}

#while loop true statment
bid = True
while bid == True:
  print(logo)

#ask user for name and bid amout as input
  bidders_name = input("What is your name? ")
  bid_amount = int(input("Enter your bid amount: "))

#update empty dictionary
  bidder_dic.update({bidders_name:bid_amount}) 

#ask for other bidders as input
  other_bidders = input("Are there other bidders? type 'yes' or 'no'\n").lower()

#clear board to wipe inputted amount off screen
  if other_bidders == "yes":
    clear()
  elif other_bidders == "no":
    clear()

# get max key and values
    max_key = max(bidder_dic, key=bidder_dic.get)
    max_value = max(bidder_dic.values())

#print the max values  
    print(f"{max_key} is the winning bidder with ${max_value}.\n" )
    
#ask for restart  
    restart_bid = input("Would you like to start a new silent bid 'yes' or 'no'? ")
    if restart_bid == "no":
      bid = False
    else:
      bid = True  