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
    for row in range(1, num_rows + 1):
        print("   ", end = "")
        print(("+-" * num_columns) + "+" )
        print(" {row} ".format(row = row), end = "")
        for column in range(1, num_columns + 1):
            pos = str(row) + ',' + str(column)
            print("|{data}".format(data = board[pos]), end = "")
        print("|")
    print("+-+" * num_columns)

board1 = init_board(6, 7)
print_board(board1, 6, 7)
