from random import randrange 


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

                    display_board(board)
                    valid = True
                    break
                else:
                    print(f"\tThe box {move} already occupied")
            else: 
                print("\tEnter integers between 1 and 9")

        except ValueError:
            print("\tEnter only integers from 1 to 9")


print("\n\t============== Start the game tic-tac-toe ==============\n")

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# board[randrange(3)][randrange(3)] = 'X'

display_board(board)
print(make_list_of_free_fields(board))
# winner = victory_for(board)
# free_fields = make_list_of_free_fields(board)

# while winner == '' and len(free_fields) > 0:
enter_move(board)
