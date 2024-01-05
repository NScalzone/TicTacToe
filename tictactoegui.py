import PySimpleGUI as sg
"""
This program uses the same logic as my basic terminal version,
but adds a GUI interface for the board. I used a video by "The CS Classroom"
on YouTube to help me build the GUI. The biggest difference between my code and theirs
is the function that checks for wins. In mine, I determined it was
only necessary to check if the most recent move resulted in a win, rather than analyzing the whole
board after every move.

Video: https://www.youtube.com/watch?v=q7Q1EQ1dZdM&t=809s&ab_channel=TheCSClassroom
"""
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

# Create the game board GUI
for row in range(3):
    newrow = []
    for column in range(3):
        newrow.append(sg.Button(size=(4,4), key=(row,column)))
    layout.append(newrow)
layout.append([sg.Button('Play Again'), sg.Button('Cancel')])

window = sg.Window('TicTacToe', layout, use_default_focus=False)

# Turn and game over help drive the gameplay loop, and determine which
# player's turn it is.
turn = 1
game_over = False

while not game_over:
    event, values = window.read()
    
    # If the user closes the window, end the program
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    # When Play Again is selected, reset the game to the beginning
    if event == 'Play Again':
        board = {}
        for row in range(3):
            for column in range(3):
                window[row,column].update('')
        turn = 1
        game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
                
    # Gameplay loop
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
