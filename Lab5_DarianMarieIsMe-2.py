'''
Lab 5 - Programming Assignment Option 2
Darian Marie Bruce
This is a game to pick up a various amount of sticks and whover picks up the last one
wins
02/12/2026
'''

#game variables

sticks = 13

sticksmin = 1

sticksmax = 4

player1_turn = True

invalid_print = "This is an invalid value. Please try again."

input_instructions = "\nEnter the amount of sticks you want to pick up."

valid_input_instructions = f"The value can only be between {sticksmin} and {sticksmax}."

sticks_left = f"There are {sticks} sticks left."

#game instructions

print("Welcome to Pick Up Sticks.\nThis game is for 2 players. \nEach player will",
      f"take turns picking up from\n{sticksmin} to {sticksmax} sticks from a pile of 13 sticks.",
      "\nWhoever picks up the last stick wins!")

while sticks > 0:
    if player1_turn:
        value_error = True
        print("It is player 1's turn!", input_instructions)
        while value_error:
             sticks_in_turn_amount = int(input(valid_input_instructions))
             if not (1 <= sticks_in_turn_amount <= 4 and sticks_in_turn_amount >= sticks):
                print(invalid_print)
             else:
                 sticks = sticks - sticks_in_turn_amount
                 print(sticks_left)
                 player1_turn = False
                 value_error = False
    else:
        print("It is player 2's turn!", input_instructions)
        value_error = True
        while value_error: 
            sticks_in_turn_amount = int(input(valid_input_instructions))
            if not (1 <= sticks_in_turn_amount <= 4 and sticks_in_turn_amount >= sticks):
                print(invalid_print)
            else:
                sticks = sticks - sticks_in_turn_amount
                print(sticks_left)
                value_error = False
                player1_turn = True

