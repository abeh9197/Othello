def get_move(board, player):
    """
    ユーザーからの入力を受け取り、x座標とy座標を返す関数
    """
    while True:
        try:
            move = input("Enter your move (row, col): ")
            row, col = move.split(',')
            row = int(row.strip())
            col = int(col.strip())
            if row < 0 or row > 7 or col < 0 or col > 7:
                print("Invalid move. Please try again.")
            elif board[row][col] != ' ':
                print("There is already a piece there. Please try again.")
            else:
                if is_valid_move(board, player, row, col):
                    return row, col
                else:
                    print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def is_valid_move(board, player, row, col):
    """
    指定された座標が有効な手かどうかを判定する関数
    """
    if board[row][col] != ' ':
        return False

    other_player = 'X' if player == 'O' else 'O'

    # 指定された座標の周り8方向に対して、ひっくり返せる石があるかどうかを判定する
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r = row + dr
            c = col + dc
            if r < 0 or r > 7 or c < 0 or c > 7:
                continue
            if board[r][c] == other_player:
                while True:
                    r += dr
                    c += dc
                    if r < 0 or r > 7 or c < 0 or c > 7:
                        break
                    if board[r][c] == player:
                        return True
                    elif board[r][c] == ' ':
                        break
    return False

def make_move(board, player, row, col):
    """
    指定された座標に石を置き、ひっくり返す関数
    """
    board[row][col] = player
    other_player = 'X' if player == 'O' else 'O'
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r = row + dr
            c = col + dc
            if r < 0 or r > 7 or c < 0 or c > 7:
                continue
            if board[r][c] == other_player:
                pieces_to_flip = []
                while True:
                    pieces_to_flip.append((r, c))
                    r += dr
                    c += dc
                    if r < 0 or r > 7 or c < 0 or c > 7:
                        break
                    if board[r][c] == player:
                        for flip_row, flip
