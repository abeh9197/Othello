import readchar

def print_board(board, cursor_row, cursor_col):
    print("  1 2 3 4 5 6 7 8")
    print(" +-+-+-+-+-+-+-+-+")
    for i in range(len(board)):
        row = str(i+1) + "|"
        for j in range(len(board[i])):
            if i == cursor_row and j == cursor_col:
                row += "*|"
            elif board[i][j] == 1:
                row += "●|"
            elif board[i][j] == -1:
                row += "○|"
            else:
                row += " |"
        print(row)
        print(" +-+-+-+-+-+-+-+-+")

# Example usage
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, -1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
cursor_row = 3
cursor_col = 3
print_board(board, cursor_row, cursor_col)

while True:
    key = readchar.readkey()
    if key == readchar.key.UP:
        cursor_row = max(0, cursor_row-1)
    elif key == readchar.key.DOWN:
        cursor_row = min(len(board)-1, cursor_row+1)
    elif key == readchar.key.LEFT:
        cursor_col = max(0, cursor_col-1)
    elif key == readchar.key.RIGHT:
        cursor_col = min(len(board[0])-1, cursor_col+1)
    elif key == '\r':
        # Enter key pressed
        break
    print_board(board, cursor_row, cursor_col)