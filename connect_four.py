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
    if column > num_columns:
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

def check_board_rows(board, num_rows, num_columns):
    # check rows
    for row in range(1, num_rows + 1):
        count_x = 0
        count_o = 0
        for column in range(1, num_columns + 1):
            pos = str(row) + ',' + str(column)
            if board[pos] == " ":
                count_x = 0
                count_y = 0
            elif board[pos] == "x":
                count_x += 1
                count_o = 0
            elif board[pos] == "o":
                count_o += 1
                count_x = 0
            # check four
            if count_x == 4:
                return "x"
            elif count_o == 4:
                return "o"

    return "c"

def check_board_columns(board, num_rows, num_columns):
    # check columns
    for column in range(1, num_columns + 1):
        count_x = 0
        count_o = 0
        for row in range(1, num_rows + 1):
            pos = str(row) + ',' + str(column)
            if board[pos] == " ":
                break
            elif board[pos] == "x":
                count_x += 1
                count_o = 0
            elif board[pos] == "o":
                count_o += 1
                count_x = 0
            # check four
            if count_x == 4:
                return "x"
            elif count_o == 4:
                return "o"
    return "c"

board1 = init_board(6, 7)
print_board(board1, 6, 7)
board1 = place_piece(board1, 1, "o",  6, 7)
print_board(board1, 6, 7)
board1 = place_piece(board1, 2, "x",  6, 7)
print_board(board1, 6, 7)
board1 = place_piece(board1, 3, "o",  6, 7)
print_board(board1, 6, 7)
status = check_board_rows(board1, 6, 7)
print(status)
status = check_board_columns(board1, 6, 7)
print(status)
board1 = place_piece(board1, 4, "x",  6, 7)
print_board(board1, 6, 7)
status = check_board_rows(board1, 6, 7)
print(status)
status = check_board_columns(board1, 6, 7)
print(status)
board1 = place_piece(board1, 5, "x",  6, 7)
print_board(board1, 6, 7)
status = check_board_rows(board1, 6, 7)
print(status)
status = check_board_columns(board1, 6, 7)
print(status)
board1 = place_piece(board1, 6, "x",  6, 7)
print_board(board1, 6, 7)
status = check_board_rows(board1, 6, 7)
print(status)
status = check_board_columns(board1, 6, 7)
print(status)
board1 = place_piece(board1, 7, "x",  6, 7)
print_board(board1, 6, 7)
status = check_board_rows(board1, 6, 7)
print(status)
status = check_board_columns(board1, 6, 7)
print(status)

