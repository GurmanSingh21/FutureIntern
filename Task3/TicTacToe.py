# Tic-Tac-Toe Game in Python

# Create the Tic-Tac-Toe board
board = [' ' for _ in range(9)]


# Function to print the board
def print_board():
    print('---------')
    for i in range(3):
        print(f'| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |')
        print('---------')


# Function to check for a win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical wins
        [0, 4, 8], [2, 4, 6]  # Diagonal wins
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


# Function to check for a draw
def check_draw():
    return all(cell != ' ' for cell in board)


# Function to make a move
def make_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("This spot is already taken. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a number between 1 and 9.")


# Main game loop
def play_game():
    current_player = 'X'
    while True:
        print_board()
        make_move(current_player)

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_draw():
            print_board()
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'


# Start the game
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_game()
