def init_board(num_rows, num_columns):
    board = {}
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            pos = str(row) + ',' + str(column)
            board[pos] = " "
    return board

def print_board(board, num_rows, num_columns):
    print("   ", end = "")
    for num in range(1, num_columns + 1):
        print(" {num}".format(num = num), end = "")
    print(" ")
    for row in range(num_rows, 0, -1):
        print("   ", end = "")
        print(("+-" * num_columns) + "+" )
        print(" {row} ".format(row = row), end = "")
        for column in range(1, num_columns + 1):
            pos = str(row) + ',' + str(column)
            print("|{data}".format(data = board[pos]), end = "")
        print("|")
    print("   ", end = "")
    print(("+-" * num_columns) + "+\n" )

def place_piece(board, column, piece, num_rows, num_columns):
    if column >= num_columns:
        print("Trying to place an {piece} in column {column}".format(
                piece = piece, column = column))
        print("Make sure to pick a column between 1 and {num_columns}".format(
            num_columns = num_columns))
        return board
    for row in range(1, num_rows + 1):
        pos = str(row) + ',' + str(column)
        if board[pos] == " ":
            board[pos] = piece
            return board
    print("Column {column} is full. Please pick a column that is not full".format(
        column = column))

board1 = init_board(6, 7)
print_board(board1, 6, 7)
board1 = place_piece(board1, 1, "x",  6, 7)
print_board(board1, 6, 7)

