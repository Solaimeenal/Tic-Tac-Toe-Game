import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

# Function to make a move for the computer
def make_computer_move(board, player):
    # Simple AI: Choose the first available move
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                return

# Main function to play Tic Tac Toe
def play_tictac():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    print("Tic Tac Game")
    mode = input("Choose mode: (1) Player vs. Player, (2) Player vs. Computer: ")
    
    # Set the players
    if mode == "1":
        player1 = 'X'
        player2 = 'O'
        play_vs_computer = False
    else:
        player1 = 'X'
        player2 = 'O'
        play_vs_computer = True
    
    current_player = player1
    
    # Start the game loop
    while True:
        print_board(board)
        
        if current_player == player1 or not play_vs_computer:
            # Player's turn
            row = int(input(f"Player {current_player}, enter the row (0-2): "))
            col = int(input(f"Player {current_player}, enter the column (0-2): "))
            
            if board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
            
            board[row][col] = current_player
        else:
            # Computer's turn
            print(f"Computer's turn ({current_player}):")
            make_computer_move(board, current_player)
        
        # Check if the current player wins
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = player2 if current_player == player1 else player1

play_tictac()
