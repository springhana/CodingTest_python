row, col = map(int, input().split())
board = []
result = []

for _ in range(row):
    board.append(input())

for i in range(row - 7):
    for j in range(col - 7):
        draw1 = 0
        draw2 = 0
        for a in range(i + 8):
            for b in range(j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] == "W":
                        draw1 += 1
                    if board[a][b] == "B":
                        draw2 += 1
                else:
                    if board[a][b] == "B":
                        draw1 += 1
                    if board[a][b] == "W":
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)

print(min(result))
