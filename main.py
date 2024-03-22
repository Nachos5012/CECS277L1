# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 01/29/2024
# Module 1 - Shell game
# importing the random module

import check_input
import random


def main():
  print("-Shell Game-")
  print("Find the ball to double your bet!")
  amount = 100

  while amount > 0:
    print("\nYou have $" + str(amount))
    if amount < 50:
      bet = check_input.get_int_range("Bet amount? ", 1, amount)
    else:
      bet = check_input.get_int_range("Bet amount? ", 1, 50)
    
    ball_position = random.randint(1, 3)
    print("  ---     ---     ---")
    print(" /   \   /   \   /   \ ")
    print("/  1  \ /  2  \ /  3  \ ")
    print("_______ _______ _______")
    guess = check_input.get_int_range("Make a guess: ", 1, 3)
    
    if ball_position == 1:
      print("  ---     ---     ---")
      print(" /   \   /   \   /   \ ")
      print("/  o  \ /     \ /     \ ")
      print("_______ _______ _______")
    elif ball_position == 2:
      print("  ---     ---     ---")
      print(" /   \   /   \   /   \ ")
      print("/     \ /  o  \ /     \ ")
      print("_______ _______ _______")
    else:
      print("  ---     ---     ---")
      print(" /   \   /   \   /   \ ")
      print("/     \ /     \ /  o  \ ")
      print("_______ _______ _______")
    
    if guess == ball_position:
      print("Congratulations!\n")
      amount = amount + bet
    else:
      print("Sorry... You lose.")
      amount = amount - bet
    if amount > 0:
      repeat = check_input.get_yes_no("Play again? (Y/N): ")
      if repeat:
        continue
      else:
        break
  
  print("You're out of money! Game over.")

main()

