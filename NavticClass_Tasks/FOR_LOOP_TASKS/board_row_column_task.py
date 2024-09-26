EMPTY = "-"
ROOK = "ROOK"
world="world"
laptop="laptop"
book="book"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = laptop
board[7][0] = world
board[7][7] = ROOK
board[0][5] = book
board[1][6] = laptop

for row in board:
    for item in row:
      print(item,end=" ")
    print()

