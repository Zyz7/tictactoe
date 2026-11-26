from random import randrange 
from random import choice

def display_board(board):
    # The function accepts a parameter which contains the current state of the board 
    # and shows it on the console.
    for i in range(3):
        print("\t\t\t+-------+-------+-------+")

        for j in range(3):
            if j == 1:
                print(f"\t\t\t|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |")
            else:
                print("\t\t\t|       |       |       |")

    print("\t\t\t+-------+-------+-------+")



def make_list_of_free_fields(board):
    # The function examines the board and builds a list of all empty boxes. 
    # The list is made up of tuples, each tuple is a pair of numbers that indicate the row and column.
    free_fields = []

    for i in range(3):
        for j in range(3):
            if str(board[i][j]) != 'X' and str(board[i][j]) != 'O':
                free_fields.append(board[i][j])

    return free_fields


def winning_square(board):
    #
    numbers = []
    movements = []
    
    # Review rows
    for row in board:
        if row[0] == row[1]:
            movements.append(row[2])
        elif row[0] == row[2]:
            movements.append(row[1])
        elif row[1] == row[2]:
            movements.append(row[0])
    
    # Review columns
    for col in range(3):
        if board[0][col] == board[1][col]:
            movements.append(board[2][col])
        elif board[0][col] == board[2][col]:
            movements.append(board[1][col])
        elif board[1][col] == board[2][col]:
            movements.append(board[0][col])
    
    # Review diagonals
    if board[0][0] == board[1][1]:
        movements.append(board[2][2])
    elif board[0][0] == board[2][2]:
        movements.append(board[1][1])
    elif board[1][1] == board[2][2]:
        movements.append(board[0][0])
    
    if board[0][2] == board[1][1]:
        movements.append(board[2][0])
    elif board[0][2] == board[2][0]:
        movements.append(board[1][1])
    elif board[1][1] == board[2][0]:
        movements.append(board[0][2])

    numbers = [z for z  in movements if isinstance(z, int)]
    return list(set(numbers))
    

def enter_move(board):
    # The function accepts the current state of the board and asks the user about its movement, 
    # verifies the input and updates the dashboard according to the user's decision.
    valid = False
    free_fields = make_list_of_free_fields(board)

    while len(free_fields) > 0 and valid == False:
        try:    
            move = int(input("\n\tEnter your movement: "))

            if move >= 1 and move <= 9:
                if move in free_fields:
                    for i, row in enumerate(board):
                        if move in row :
                            board[i][row.index(move)] = 'O'

                    print("")
                    display_board(board)
                    valid = True
                    break
                else:
                    print(f"\tThe box {move} already occupied")
            else: 
                print("\tEnter integers between 1 and 9")

        except ValueError:
            print("\tEnter only integers from 1 to 9")


def draw_move(board):
    # The function draws the movement of the machine and updates the board.
    # prioritize = [1, 3, 5, 7, 9]
    prioritize = winning_square(board)
    free_fields = make_list_of_free_fields(board)

    if len(free_fields) > 0:
        print("\n\tThe machine enters its movement: ")

        found = [n for n in prioritize if n in free_fields]
        if len(found) > 0:
            print(winning_square(board))
            move = choice(found)
        else:
            print(winning_square(board))
            move = choice(free_fields)

        for i, row in enumerate(board):
            if move in row :
                board[i][row.index(move)] = 'X'
                break

        print("")
        display_board(board)


def victory_for(board):
    # The function analyzes the status of the board to check if 
    # the player who uses the 'O's or the 'X's has won the game.
    winner = ''

    # Review rows
    for row in board:
        if row[0] == row[1] == row[2]:
            winner = row[0]

    # Review columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            winner = board[0][col]

    # Review diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]

    return winner


print("\n\t============== Start the game tic-tac-toe ==============\n")

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
display_board(board)

for i in range(9):
    winner = victory_for(board)

    if winner:
        break    
    enter_move(board)
    draw_move(board)
    
if winner == 'X':
    print("\n\tThe winner is: the machine")
elif winner == 'O':
    print("\n\tThe winner is: the user!")
else: 
    print("\n\tThis is a tie")
        

print("\n\t============== End of the game tic-tac-toe ==============\n")
