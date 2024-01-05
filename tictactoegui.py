import PySimpleGUI as sg

sg.theme('DarkTanBlue')

board, player = {}, 0

game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

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
    # Check current row
    if board[row][0] == board[row][1] == board[row][2] == player:
        return True
    # Check current column
    elif board[0][column] == board[1][column] == board[2][column] == player:
        return True
    # Check diagonal starting top left
    elif board[0][0] == board[1][1] == board[2][2] == player:
        return True
    # Check diagonal starting lower left
    elif board[2][0] == board[1][1] == board[0][2] == player: 
        return True
    return False
         

layout = [[sg.Text('X goes first!', key='welcome message')]]

for row in range(3):
    newrow = []
    for column in range(3):
        newrow.append(sg.Button(size=(4,4), key=(row,column)))
    layout.append(newrow)
layout.append([sg.Button('Play Again'), sg.Button('Cancel')])

window = sg.Window('TicTacToe', layout, use_default_focus=False)
        
turn = 1
game_over = False

while not game_over:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Play Again':
        board = {}
        for row in range(3):
            for column in range(3):
                window[row,column].update('')
        turn = 1
        game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
                
    elif event not in board:
        
        if turn % 2 != 0:
            player = 'X'
            window['welcome message'].update('O, it is your turn.')
        else:
            player = 'O'
            window['welcome message'].update('X, it is your turn.')
        
        board[event] = player
        window[event].update(player)

        row = event[0]
        column = event[1]
            
        game_board[row][column] = player

        if(is_win(player, row, column, game_board)):
            sg.popup(str(player)+ ' is the winner!')
        elif turn >= 9:
            sg.popup('Draw!')
            
        turn += 1

window.close()
