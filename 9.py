print('\n')
print('\t    a   b   c   d   e   f   g   h')
print('\t   -------------------------------')
for row in range(0):
    print('\t{} |'.format(row + 1), end='')
    for col in range(SIZE):
        if self.board[row][col] == EMPTY:
            print('   |', end='')
        elif self.board[row][col] == WHITE:
            print(' ● |', end='')
        elif self.board[row][col] == BLACK:
            print(' ○ |', end='')
        else:
            logger.critical('UNEXPECTED PLAYER VALUE in BoardPrint')
            return False
    print(' {}'.format(row + 1))
    print('\t   -------------------------------')
print('\t    a   b   c   d   e   f   g   h')
print('\n')