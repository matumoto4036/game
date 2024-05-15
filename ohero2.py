import random

def print_board(board):
    print("  a b c d e f g h")
    print(" +----------------")
    for i in range(8):
        print(f"{i+1}|", end="")
        for j in range(8):
            print(board[i][j], end=" ")
        print("|")
    print(" +----------------")

def initialize_board():
    board = [["." for _ in range(8)] for _ in range(8)]
    board[3][3] = board[4][4] = 'W'
    board[3][4] = board[4][3] = 'B'
    return board

def is_valid_move(board, player, row, col):
    if board[row][col] != '.' or not (0 <= row < 8 and 0 <= col < 8):
        return False

    opponent = 'W' if player == 'B' else 'B'
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for d in directions:
        r, c = row + d[0], col + d[1]
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            r += d[0]
            c += d[1]
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                r += d[0]
                c += d[1]
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                return True
    return False

def make_move(board, player, row, col):
    if not is_valid_move(board, player, row, col):
        return False

    board[row][col] = player
    opponent = 'W' if player == 'B' else 'B'
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for d in directions:
        r, c = row + d[0], col + d[1]
        if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
            pieces_to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                pieces_to_flip.append((r, c))
                r += d[0]
                c += d[1]
            if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == player:
                for pr, pc in pieces_to_flip:
                    board[pr][pc] = player
    return True

def get_valid_moves(board, player):
    return [(r, c) for r in range(8) for c in range(8) if is_valid_move(board, player, r, c)]

def get_ai_move(board, player):
    valid_moves = get_valid_moves(board, player)
    return random.choice(valid_moves) if valid_moves else None

def get_player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (e.g., 'e6'), or '0' for a random move: ")
        if move == '0':
            valid_moves = get_valid_moves(board, player)
            if not valid_moves:
                return None  # No valid moves available
            return random.choice(valid_moves)
        else:
            if len(move) != 2 or not move[0].isalpha() or not move[1].isdigit():
                print("Invalid input. Please enter a column followed by a row (e.g., 'e6'), or '0' for a random move.")
                continue
            col = ord(move[0].lower()) - ord('a')
            row = int(move[1]) - 1
            if is_valid_move(board, player, row, col):
                return row, col
            else:
                print("Invalid move. Please try again.")

def game_over(board):
    return get_valid_moves(board, 'B') == [] and get_valid_moves(board, 'W') == []

def count_pieces(board):
    black_count = sum(row.count('B') for row in board)
    white_count = sum(row.count('W') for row in board)
    return black_count, white_count

def main():
    board = initialize_board()
    player = 'B'  # Black starts
    while not game_over(board):
        print_board(board)
        if player == 'B':
            row, col = get_player_move(board, player)  # Get human player's move
        else:
            move = get_ai_move(board, player)  # Get AI's move
            if move is None:
                print("AI has no valid moves. Skipping turn.")
                player = 'B'
                continue
            row, col = move
            print(f"AI plays: {chr(col + ord('a'))}{row + 1}")

        if row is None:
            print(f"Player {player} has no valid moves. Skipping turn.")
        else:
            make_move(board, player, row, col)

        player = 'W' if player == 'B' else 'B'  # Switch players

    # Game is over, print final board and score
    print_board(board)
    black_count, white_count = count_pieces(board)
    print(f"Final score: B: {black_count} - W: {white_count}")
    if black_count > white_count:
        print("Black wins!")
    elif black_count < white_count:
        print("White wins!")
    else:
        print("It's a tie!")

# Start the game
if __name__ == "__main__":
    main()