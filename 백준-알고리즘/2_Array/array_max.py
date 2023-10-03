rows = []
max_num = 0
max_array = []
for _ in range(9):
    col = list(map(int, input().split()))
    rows.append(col)
    max_array.append(max(col))

max_num = max(max_array)

print(max_num)

for row in range(9):
    for col in range(9):
        if rows[row][col] == max_num:
            print(row + 1, col + 1, end=' ')
