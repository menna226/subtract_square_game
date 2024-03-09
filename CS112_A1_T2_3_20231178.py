# File: CS112_A1_T2_3_20231178.py
# Purpose: in this problem player1 and player2 have to enter a number and take turns subtracting a square number from the orginal one. the winner is the one who subtracts the last square number.
# Author: Menna Abdallah Helmi
# ID: 20231178

import math
import random

print('********** Welcome to the Subtract Number Game **********\n')

coins = 0            # Number of coins in the pile
current_player = 0   # Tracks the current player
chosen_number = 0    # The number chosen by the player to subtract from the pile

# Function to validate integer input
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter an integer.")

# Choosing a number: user input or random number
choice = ''
while choice not in ['N', 'R']:
    choice = input("Please enter 'N' to insert a number or 'R' for a randomly generated number: ").upper()
    if choice == 'N':
        coins = get_integer_input("Please enter a non-square number of coins to subtract from: ")
    else:
        coins = random.randint(10, 1000)

# Ensuring the number of coins is not a perfect square
while math.sqrt(coins).is_integer():
    if choice == 'N':
        coins = get_integer_input("Invalid input. Please enter a non-square number of coins to subtract from: ")
    else:
        coins = random.randint(10, 1000)

# Game loop
while coins != 0:
    # Taking input from the player
    print(f"\nIt's player {current_player + 1}'s turn.\nRemaining coins in the pile: {coins}")
    chosen_number = get_integer_input("Please enter a square number to subtract: ")
    
    # Validating the chosen number
    if chosen_number > coins:
        print("Invalid input. The chosen number exceeds the remaining coins in the pile.")
        continue
    
    if not math.sqrt(chosen_number).is_integer():
        print("Invalid input. Please enter a valid square number.")
        continue

    # Subtracting the chosen number from the pile
    coins -= chosen_number

    # Switching players
    current_player = 1 - current_player

# Printing the winner
print(f"The winner is player {1-current_player + 1}") # current player is storing the loser so we subtract current player from  1 then we add 1 to strart naming the players correctly (if current player is assigned to 0 so player 1 is the winner and if current player is assigned to 1 then player 2 is the winner) 
print("**********************************************************")