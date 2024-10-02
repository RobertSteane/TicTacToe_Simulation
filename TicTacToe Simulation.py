import random

# Create the basis for the tictactoe grid
tictactoe_grid = [ '','','','','','','','','']

# No one has won at the start of the game
win_points = 0
# The game hasn't finished yet
game_status = 0

# Define which player is going first
player_turn = input('''Please pick strategy "1" or strategy "2"'''.strip().lower())

# Define a function to assign points to the winner
def win_points_change(symbol):
    global win_points
    if symbol == "x":
        win_points += 1
    if symbol == "o":
        win_points += 2

# Define a function to check if the game has ended yet due to a player winning
def end_check():
    global game_status
    if win_points == 1 or win_points == 2:
        game_status = 1

def win_condition():
    for i in ['x', 'o']:
        # Check rows, columns, and diagonals
        if (tictactoe_grid[0] == i and tictactoe_grid[1] == i and tictactoe_grid[2] == i) or \
           (tictactoe_grid[3] == i and tictactoe_grid[4] == i and tictactoe_grid[5] == i) or \
           (tictactoe_grid[6] == i and tictactoe_grid[7] == i and tictactoe_grid[8] == i) or \
           (tictactoe_grid[0] == i and tictactoe_grid[3] == i and tictactoe_grid[6] == i) or \
           (tictactoe_grid[1] == i and tictactoe_grid[4] == i and tictactoe_grid[7] == i) or \
           (tictactoe_grid[2] == i and tictactoe_grid[5] == i and tictactoe_grid[8] == i) or \
           (tictactoe_grid[0] == i and tictactoe_grid[4] == i and tictactoe_grid[8] == i) or \
           (tictactoe_grid[2] == i and tictactoe_grid[4] == i and tictactoe_grid[6] == i):
            win_points_change(i)
            return True  # Indicate that there is a winner
    return False  # No winner

# function to progress the game with players taking alternating turns
def turn_tracker():
    global player_turn
    if player_turn == "1":
        strategy_1()
        player_turn = "2"
    elif player_turn == "2":
        strategy_2()
        player_turn = "1"
    end_check()

# Strategy number 1
def strategy_1():
    global tictactoe_grid
    empty_positions = [index for index, value in enumerate(tictactoe_grid) if value == '']

    if not empty_positions:
        print("No empty positions left for Strategy 1 .")
        return
    
    else: 
        random_choice = random.choice(empty_positions)
        tictactoe_grid[random_choice] = "x"
        print(f"Strategy 1 chose position {random_choice}.")

# Strategy number 2
def strategy_2():
    global tictactoe_grid
    empty_positions = [index for index, value in enumerate(tictactoe_grid) if value == '']
    
    if not empty_positions:
        print("No empty positions left for Streatgy 2.")
        return
    else:
        random_choice = random.choice(empty_positions)
        tictactoe_grid [random_choice] = "o"
        print(f"Strategy 2 chose position {random_choice}.")

while True:
    turn_tracker()
    print("Current board:", tictactoe_grid)  # Print the current state of the grid
    if win_condition():
        if win_points == 1:
            print(f"Game over! The winner was Strategy 1!")
            break  # Exit loop if there's a winner 
        if win_points == 2:
            print(f"Game over! The winner was Strategy 2!")
            break  # Exit loop if there's a winner
    if all(cell != '' for cell in tictactoe_grid):  # Check for a draw
        print("It's a draw!")
        break  # Exit loop if the grid is full