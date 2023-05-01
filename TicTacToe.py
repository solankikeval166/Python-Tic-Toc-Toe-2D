# Printing the game board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_win(board, player):
    # """Checks if the player has won the game."""
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

# main function to rumn app
def tic_tac_toe():
    board = [[" ", " ", " "] for i in range(3)]
    players = ["X", "O"]
    current_player = 0
    while True:
        print_board(board)
        player_choice = input(f"Player {players[current_player]}, enter a row and column number (e.g. 1 2): ")
        row, col = map(int, player_choice.split())
        if board[row-1][col-1] != " ":
            print("That space is already taken. Try again.")
            continue
        board[row-1][col-1] = players[current_player]
        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        if all(" " not in row for row in board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = (current_player + 1) % 2

# Run the game
tic_tac_toe()
