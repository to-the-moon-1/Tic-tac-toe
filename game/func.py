from copy import deepcopy


def turn_o(board):
    count_o = 0
    count_x = 0
    for bb in board:
        for b in bb:
            if b == "O":
                count_o += 1
            if b == "X":
                count_x += 1
    if count_x == count_o + 1:
        return select_space(board, minimax(board, False)[1], "O")


def select_space(board, move, turn):
    if move not in range(1, 10):
        return False
    row = int((move - 1) / 3)
    col = (move - 1) % 3
    if board[row][col] != "X" and board[row][col] != "O":
        board[row][col] = turn
        return True
    else:
        return False


def available_moves(board):
    moves = []
    for row in board:
        for col in row:
            if col != "X" and col != "O":
                moves.append(int(col))
    return moves


def has_won(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def game_is_over(board):
    return (has_won(board, "X") and "Player-X won!") or (has_won(board, "O") and "Player-O won!") or (len(available_moves(board)) == 0 and "It's tie!")


def evaluate_board(board):
    if has_won(board, "X"):
        return 1
    elif has_won(board, "O"):
        return -1
    else:
        return 0


def minimax(input_board, is_maximizing):
    # Base case - the game is over, so we return the value of the board
    if game_is_over(input_board):
        return [evaluate_board(input_board), ""]
    # The maximizing player
    if is_maximizing:
        # The best value starts at the lowest possible value
        best_value = -float("Inf")
        best_move = ""
        # Loop through all the available moves
        for move in available_moves(input_board):
            # Make a copy of the board and apply the move to it
            new_board = deepcopy(input_board)
            select_space(new_board, move, "X")
            # Recursively find your opponent's best move
            hypothetical_value = minimax(new_board, False)[0]
            # Update best value if you found a better hypothetical value
            if hypothetical_value > best_value:
                best_value = hypothetical_value
                best_move = move
        return [best_value, best_move]
    # The minimizing player
    else:
        # The best value starts at the highest possible value
        best_value = float("Inf")
        best_move = ""
        # Testing all potential moves
        for move in available_moves(input_board):
            # Copying the board and making the move
            new_board = deepcopy(input_board)
            select_space(new_board, move, "O")
            # Passing the new board back to the maximizing player
            hypothetical_value = minimax(new_board, True)[0]
            # Keeping track of the best value seen so far
            if hypothetical_value < best_value:
                best_value = hypothetical_value
                best_move = move
        return [best_value, best_move]
