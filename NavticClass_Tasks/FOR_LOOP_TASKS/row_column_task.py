board = []
EMPTY = "E"
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

# print(board)
# for board in row:
#     for element in row:
#         print(element, end=" ")
#     print()

board[2][6] = "W"
for row in board:
    print(row)