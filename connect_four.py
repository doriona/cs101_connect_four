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
    if column > num_columns or column < 1:
        print("Trying to place an {piece} in column {column}".format(
                piece = piece, column = column))
        print("Make sure to pick a column between 1 and {num_columns}".format(
            num_columns = num_columns))
        return -1, board
    for row in range(1, num_rows + 1):
        pos = str(row) + ',' + str(column)
        if board[pos] == " ":
            board[pos] = piece
            return 0, board
    print("Column {column} is full. Please pick a column that is not full".format(
        column = column))
    return -1, board

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

def check_board_diagonals_column(board, num_rows, num_columns):
    # check diagonals from column
    for column_main in range(1, num_columns + 1):
        # down to up
        count_x = 0
        count_o = 0
        row = 1
        column = column_main
        while (row < num_rows + 1) and (column < num_columns + 1):
            pos = str(row) + ',' + str(column)
            if board[pos] == " ":
                count_x = 0
                count_o = 0
            elif board[pos] == "x":
                count_x += 1
                count_o = 0
            elif board[pos] == "o":
                count_x = 0
                count_o += 1
            # check four
            if count_x == 4:
                return "x"
            elif count_o == 4:
                return "o"
            row += 1
            column += 1
        # up to down
        count_x = 0
        count_o = 0
        row = num_rows
        column = column_main
        while (row >= 1) and (column < num_columns + 1):
            pos = str(row) + ',' + str(column)
            if board[pos] == " ":
                count_x = 0
                count_o = 0
            elif board[pos] == "x":
                count_x += 1
                count_o = 0
            elif board[pos] == "o":
                count_x = 0
                count_o += 1
            # check four
            if count_x == 4:
                return "x"
            elif count_o == 4:
                return "o"
            row -= 1
            column += 1
    return "c"

def check_board_diagonals_row(board, num_rows, num_columns):
    # check diagonals from rows
    for row_main in range(1, num_rows + 1):
        # down to up
        count_x = 0
        count_o = 0
        row = row_main
        column = 1
        while (row < num_rows + 1) and (column < num_columns + 1):
            pos = str(row) + ',' + str(column)
            if board[pos] == " ":
                count_x = 0
                count_o = 0
            elif board[pos] == "x":
                count_x += 1
                count_o = 0
            elif board[pos] == "o":
                count_x = 0
                count_o += 1
            # check four
            if count_x == 4:
                return "x"
            elif count_o == 4:
                return "o"
            row += 1
            column += 1
        # up to down
        count_x = 0
        count_o = 0
        row = row_main
        column = 1
        while (row >= 1) and (column < num_columns + 1):
            pos = str(row) + ',' + str(column)
            if board[pos] == " ":
                count_x = 0
                count_o = 0
            elif board[pos] == "x":
                count_x += 1
                count_o = 0
            elif board[pos] == "o":
                count_x = 0
                count_o += 1
            # check four
            if count_x == 4:
                return "x"
            elif count_o == 4:
                return "o"
            row -= 1
            column += 1
    return "c"

def check_full(board, num_rows, num_columns):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            pos = str(row) + ',' + str(column)
            if board[pos] == " ":
                return "c"
    return "t"

def check_board(board, num_rows, num_columns):
    status = check_board_rows(board, num_rows, num_columns)
    print("checking rows: {status}".format(status = status))
    if status != "c":
        return status
    status = check_board_columns(board, num_rows, num_columns)
    print("checking columns: {status}".format(status = status))
    if status != "c":
        return status
    status = check_board_diagonals_column(board, num_rows, num_columns)
    print("checking diagonals column: {status}".format(status = status))
    if status != "c":
        return status
    status = check_board_diagonals_row(board, num_rows, num_columns)
    print("checking diagonals row: {status}".format(status = status))
    if status != "c":
        return status
    status = check_full(board, num_rows, num_columns)
    print("checking full board: {status}".format(status = status))
    if status != "c":
        return status
    return "c"

def get_move(piece, num_columns):
    message = "Please enter a column number for player {piece} (between 1 and {num_columns}): "
    column = input(message.format(piece = piece, num_columns = num_columns))
    return int(column)

def play_game(num_rows, num_columns):
    board1 = init_board(num_rows, num_columns)
    print_board(board1, num_rows, num_columns)
    status = 'c'
    pieces = ['x','o']
    piece_index = 0
    while (status == 'c'):
        column = get_move(pieces[piece_index], 7)
        column_error, board1 = place_piece(board1, column, pieces[piece_index], num_rows, num_columns)
        if column_error == -1:
            continue
        print_board(board1, num_rows, num_columns)
        status = check_board(board1, num_rows, num_columns)
        if piece_index == 0:
            piece_index = 1
        else:
            piece_index = 0
    if status == "x":
        print("Player x won!")
        return 0
    elif status == "o":
        print("Player o won!")
        return 0
    elif status == "t":
        print("It is a tie!")
        return 0
    return 1

num_rows = 6
num_columns = 7
game_status = 0
game_init = 'y'
while game_init != 'n' and game_status == 0:
    game_init = input("Do you want to play to connect four? [y/n]]: ")
    if game_init == 'y':
        game_status = play_game(num_rows, num_columns)


# Example game
#board1 = init_board(6, 7)
#print_board(board1, 6, 7)
#board1 = place_piece(board1, 1, "o",  6, 7)
#print_board(board1, 6, 7)
#board1 = place_piece(board1, 2, "x",  6, 7)
#print_board(board1, 6, 7)
#board1 = place_piece(board1, 2, "o",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 3, "x",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 3, "x",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 3, "o",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 4, "x",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 4, "x",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 4, "o",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 4, "x",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 1, "x",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 1 , "x",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 1, "x",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
#board1 = place_piece(board1, 2, "x",  6, 7)
#print_board(board1, 6, 7)
#status = check_board(board1, 6, 7)
