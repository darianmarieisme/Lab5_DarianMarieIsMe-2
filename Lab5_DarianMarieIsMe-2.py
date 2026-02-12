'''
Lab 5 - Programming Assignment Option 2
Darian Marie Bruce
This is a game to pick up a various amount of sticks and whover picks up the last one
wins
02/12/2026
'''

#game variables

sticks = 13

min = 1

max = 4

player1_turn = True

value_error = True

#game instructions

print("Welcome to Pick Up Sticks.\nThis game is for 2 players. \nEach player will",
      f"take turns picking up from\n{min} to {max} sticks from a pile of 13 sticks.",
      "\nWhoever picks up the last stick wins!")

while sticks > 0:
    if player1_turn:
        print("It is player 1's turn!"
              ,"\nEnter the amount of sticks you want to pick up.")
        while value_error:
             player1 = int(input(f"The value can only be between {min} and {max}."))
             if not (1 <= player1 <= 4):
                print("This is an invalid value. Please try again.")
             else:
                 sticks = sticks - player1
                 print(f"There are {sticks} left.")
                 value_error = False
            
