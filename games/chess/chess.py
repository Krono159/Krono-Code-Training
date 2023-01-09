markup = 'A','B','C','D','E','F','G','H'
initial_board = [    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]
lock = False
board = initial_board
def is_legal_move(board, start_row, start_col, end_row, end_col):
    # get the piece being moved
    piece = board[start_row][start_col]

    # check if the destination square is occupied by a piece of the same color
    if board[end_row][end_col] != ' ' and board[end_row][end_col].lower() == piece.lower():
        return False

    # check if the move is within the boundaries of the board
    if end_row < 0 or end_row > 7 or end_col < 0 or end_col > 7:
        return False

    # check if the piece is a pawn
    if piece == 'P' or piece == 'p':
        # pawns can only move forward (toward the opponent)
        if piece == 'P' and start_row > end_row:
            return False
        if piece == 'p' and start_row < end_row:
            return False

        # pawns can only move one square at a time, unless they are at their starting position
        if abs(start_row - end_row) > 1 and (start_row != 1 and start_row != 6):
            return False

        # pawns can only capture diagonally
        if start_col != end_col and board[end_row][end_col] == ' ':
            return False
        else:
            board[start_col][end_col] = ' '
    elif piece == 'N' or piece == 'n':
    # knights can move in an L-shape (two squares in one direction, and one square in the other)
        if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1:
            return True
        if abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2:
            return True
        return False

# check if the piece is a bishop, rook, or queen
    elif piece == 'B' or piece == 'R' or piece == 'Q' or piece == 'b' or piece == 'r' or piece == 'q':
        # bishops, rooks, and queens can move diagonally, horizontally, or vertically
        # but they can't jump over other pieces
        if start_row != end_row and start_col != end_col:
            # check if the move is diagonal
            if abs(start_row - end_row) == abs(start_col - end_col):
                # check if the squares between the start and end squares are empty
                for i in range(1, abs(start_row - end_row)):
                    if start_row < end_row and start_col < end_col:
                        if board[start_row + i][start_col + i] != ' ':
                            return False
                    elif start_row < end_row and start_col > end_col:
                        if board[start_row + i][start_col - i] != ' ':
                            return False
                   
def printboard():
    ctlt = 1
    print(" ",markup)
    for row in board:
        print(ctlt,row)
        ctlt = ctlt + 1
    ctlt = 0
def move_piece(board, start_square, end_square):
    # get the indices of the start and end squares
    start_row, start_col = get_indices(start_square)
    end_row, end_col = get_indices(end_square)
        
    # get the piece at the start square
    piece = board[start_row][start_col]

    if is_legal_move(board,start_row,start_col,end_row,end_col)!= False:
    # move the piece to the end square
        board[end_row][end_col] = piece
    # clear the start square
        board[start_row][start_col] = ' '
    else:
        print('illegal movement\n\n')

# function to convert a square notation (e.g. "A5") to indices (e.g. (0, 0))
def get_indices(square):
    col_index = ord(square[0]) - ord('A')
    row_index = int(square[1]) - 1
    return (row_index, col_index)

# move the piece at A5 to E5
move_piece(board, "A2", "A4")

while lock == False:
    move_piece(board, input("ingrese la ficha que desea mover: "), input("ingrese la posicion donde la desea mover"))
    print("\n\n\n\n\n\n\n\n\n")
    printboard()


# print the board to see the move

