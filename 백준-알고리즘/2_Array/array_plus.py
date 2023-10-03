n, m = map(int, input().split())
A, B = [], []
for _ in range(n):
    array = list(map(int, input().split()))
    A.append(array)

for _ in range(n):
    array = list(map(int, input().split()))
    B.append(array)

for row in range(n):
    for col in range(m):
        print(A[row][col] + B[row][col], end=' ')
    print()