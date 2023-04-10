def print_board(board):
    print(board[0] + "  |" + board[1] + "  |" + board[2])
    print("---+---+---")
    print(board[3] + "  |" + board[4] + "  |" + board[5])
    print("---+---+---")
    print(board[6] + "  |" + board[7] + "  |" + board[8])

def check_win(board):
    win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return True
    return False

def check_tie(board):
    if " " not in board:
        return True
    return False

def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    while True:
        print_board(board)
        print("Player " + player + " turn.")
        move = input("Enter your move (0-8): ")
        if board[int(move)] != " ":
            print("That spot is taken. Try again.")
            continue
        board[int(move)] = player
        if check_win(board):
            print_board(board)
            print("Player " + player + " wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

tic_tac_toe()
