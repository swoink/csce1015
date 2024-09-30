print ("Isabela Parra Modified This Credit Card Validator")

# Let's get the card number from the user
card_number = input("Enter your 16-digit credit card number: ")

# Check if card number is 16 digits long

# len means 'length', and the '==' is testing one thing against the other. A single equal sign would set one thing equal to the other (not what we want to do). 
# card_number.isdigit() is checking if this is numbers instead of someone typing 'cheeseburger' for their credit card number.

if len(card_number) == 16 and card_number.isdigit():     
    print ("Card is valid.")
else:
    print ("Invalid card number. It must be 16 digits long.") 
