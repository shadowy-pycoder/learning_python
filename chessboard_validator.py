from collections import Counter


def isValidChessBoard(chessboard):
    white = 0
    black = 0
    max_color = 16
    pieces = Counter(chessboard.values())
    if len(chessboard) > max_color * 2:
        print(f"Board lenghth is more than 32")
        return False
    else:
        print(f"Board lenghth is {len(chessboard)}")
    for key in chessboard.keys():
        if int(key[0]) > 8 or key[1] > 'h':
            print("Coordinates are out of 1a-8h range.")
            return False
    print("Coordinates are within 1a-8h range.")
    for value in chessboard.values():
        message = f"You can't have more than {max_color} pieces of one color"
        if value[0] == 'w':
            white += 1
            if white > max_color:
                print(message)
                return False
        elif value[0] == 'b':
            black += 1
            if black > max_color:
                print(message)
                return False
        else:
            print("Colors aren't white and black")
            return False
    print(f"Each player has at most {max_color} pieces")
    for piece, count in pieces.items():
        message = f"{piece} is out of range!"
        if piece in ['wking', 'bking', 'wqueen',
           'bqueen'] and count > 1:
            print(message)
            return False
        elif piece in ['wbishop', 'bbishop', 'wknight',
            'bknight', 'wrook', 'brook'] and count > 2:
            print(message)
            return False
        elif piece in ['wpawn', 'bpawn'] and count > 8:
            print(message)
            return False
    return True

board = {'1a': 'bking', '1f': 'wking', '1c':'brook', '3c': 'wrook', '4d': 'brook'}
print(isValidChessBoard(board))

