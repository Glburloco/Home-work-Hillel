import random
# Function to create an empty playing field


def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Game board display


def display_board(board):
    for i in range(3):
        for j in range(3):
            print(f' {board[i][j]} ', end='')
            if j < 2:
                print('|', end='')
        print()
        if i < 2:
            print('-----------')

# Checking winning combinations


def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Main function of the game


def play_game():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)
    game_over = False

    while not game_over:
        display_board(board)
        print("Ходит игрок", current_player)

        if current_player == 'X':
            row = int(input("Введите номер строки (1-3): "))
            col = int(input("Введите номер столбца (1-3): "))
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == ' ':
                board[row-1][col-1] = 'X'
                if check_win(board, 'X'):
                    display_board(board)
                    print("Выиграли Х.")
                    game_over = True
                else:
                    current_player = 'O'
            else:
                print("Недопустимый ход. Попробуйте снова.")
        else:
            computer_move(board, 'O', 'X')
            if check_win(board, 'O'):
                display_board(board)
                print("Выиграли О.")
                game_over = True
            elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                display_board(board)
                print("Ничья.")
                game_over = True
            else:
                current_player = 'X'

# Function for computer running


def computer_move(board, computer_symbol, player_symbol):
    # Проверка возможности победы компьютера
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = computer_symbol
                if check_win(board, computer_symbol):
                    return
                else:
                    board[i][j] = ' '

    # Checking the possibility of blocking a player's victory
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player_symbol
                if check_win(board, player_symbol):
                    board[i][j] = computer_symbol
                    return
                else:
                    board[i][j] = ' '

    # The computer's turn in the absence of the possibility of winning or blocking
    while True:
        row = random.randint(1, 3)
        col = random.randint(1, 3)
        if board[row-1][col-1] == ' ':
            board[row-1][col-1] = computer_symbol
            return

# Game launch


play_game()
