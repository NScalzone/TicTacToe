
game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def display_board(board):
    """
    function to display the game board in the terminal
    """
    i = 0
    while i < 3:
        print(board[i])
        i += 1

def is_legal(row, column, board):
    """
    function to determine if a move is legal
    """
    if board[row][column] == ' ':
        return True
    return False

def is_win(player,row, column, board):
    """
    Function to check after each move if the game has
    been won. We only need to check the diagonals, and the row/column
    that have most recently been played, and only for the current
    player. 
    """
    if board[row][0] == board[row][1] == board[row][2] == player:
        return True
    elif board[0][column] == board[1][column] == board[2][column] == player:
        return True
    elif board[0][0] == board[1][1] == board[2][2] == player:
        return True
    elif board[2][0] == board[1][1] == board[0][2] == player: 
        return True
    return False
         
display_board(game_board)
turn = 1
game_over = False

while game_over == False:
    if turn % 2 != 0:
        player = 'X'
    else:
        player = 'O'
    
    print(player, " it is your turn:")
    legal_move = True   
    while legal_move:
        row = int(input("Please select the row for your turn: "))
        column = int(input("Please select the column for your turn: "))
        if row > 2 or column > 2:
            print("Error, please enter values that are within the bounds")
        elif is_legal(row, column, game_board) == False:
            print("That space is already taken, please try again")
        else:
            legal_move = False
    
    game_board[row][column] = player
    
    print("current board: ")
    display_board(game_board) 
    if(is_win(player, row, column, game_board)):
        print(player, "Wins!")
        game_over = True
        
    turn += 1
