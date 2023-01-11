try:
    from msvcrt import getch
except ImportError:
    import sys
    import tty
    import termios
    def getch():
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)

# Unicode制御文字のエイリアス
EOT = chr(3)
ESC = chr(27)
SYMBOLS = {
    '\t': 'TAB',
    '\r': 'CR',
    '\n': 'LF',
}
FUNCTIONS = {
    'A': 'up-arrow',
    'B': 'down-arrow',
    'C': 'left-arrow',
    'D': 'right-arrow',
}

# メインループ
while True:
    key = getch()
    if key == EOT:
        break
    if key != ESC:
        print('keydown', SYMBOLS.get(key, key))
        continue
    key = getch()
    if key != '[':
        print('keydown ESC', SYMBOLS.get(key, key))
        continue
    key = getch()
    if key in FUNCTIONS:
        print('keydown', FUNCTIONS[key])
    else:
        print('keydown ESC [', SYMBOLS.get(key, key))