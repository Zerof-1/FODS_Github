import random

# I. List of card values
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# II. List of card suits
card_suits = ['Heart', 'Diamond', 'Club', 'Spade']

# III. Randomly pick a value and a suit
computer_value = random.choice(card_values)
computer_suit = random.choice(card_suits)

# Combine as computer's secret card
secret_card = [computer_value, computer_suit]

# IV. Ask the player to guess
print("Welcome to the Card Guessing Game!")
print("Try to guess the card...")

guess_value = input("Enter card value: ")
guess_suit = input("Enter card suit: ")

# V. Check the guess
print("\nGame Result:")

user_value = guess_value.strip().capitalize() == computer_value
user_suit = guess_suit.strip().capitalize() == computer_suit

# Responses
if user_value and user_suit:
    print("You guessed it all correctly! You win!")
elif user_value or user_suit:
    print("Close! You got one part right.")
else:
    print("Game Over! Better luck next time.")

# Reveal the correct card
print(f"The correct card was: {computer_value} of {computer_suit}")
 