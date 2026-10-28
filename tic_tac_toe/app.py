import math


HUMAN = 'X'
AI = 'O'
EMPTY = ' '

WIN_COMBINATIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
    [0, 4, 8], [2, 4, 6]             # Diagonals
]

def print_board(board):
    """Displays the current board state in a readable 3x3 grid."""
    print()
    for row in range(3):
        print(f" {board[row*3]} | {board[row*3+1]} | {board[row*3+2]} ")
        if row < 2:
            print("---+---+---")
    print()

def check_winner(board):
    """
    Checks if there's a winner or draw.
    Returns 'X', 'O', 'Draw', or None (if game is still ongoing).
    """
    for combo in WIN_COMBINATIONS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != EMPTY:
            return board[combo[0]]
            
    if EMPTY not in board:
        return 'Draw'
        
    return None

def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm for evaluating the best score for board states.
    AI ('O') is Maximizing player; Human ('X') is Minimizing player.
    """
    winner = check_winner(board)
    
    if winner == AI:
        return 10 - depth
    elif winner == HUMAN:
        return depth - 10
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, depth + 1, False)
                board[i] = EMPTY
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, depth + 1, True)
                board[i] = EMPTY
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    """Finds the optimal move for the AI using Minimax."""
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
                
    return best_move

def play_game():
    """Main interactive execution loop."""
    board = [EMPTY] * 9
    print("=" * 45)
    print(" Welcome to Tic-Tac-Toe (Human vs Unbeatable AI)")
    print("Positions are numbered 1 through 9:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("=" * 45)

    current_player = HUMAN

    while True:
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Draw':
                print(" Game Over! It's a draw!")
            elif winner == HUMAN:
                print(" Congratulations! You won!")
            else:
                print(" AI wins! Better luck next time.")
            break

        if current_player == HUMAN:
            print_board(board)
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != EMPTY:
                    print(" Invalid move! Choose an empty spot between 1 and 9.")
                    continue
                board[move] = HUMAN
                current_player = AI
            except ValueError:
                print(" Invalid input! Please enter a number from 1 to 9.")
        else:
            print("\n AI is thinking...")
            ai_move = get_best_move(board)
            board[ai_move] = AI
            current_player = HUMAN

if __name__ == "__main__":
    play_game()