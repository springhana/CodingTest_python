paper = [[0] * 101 for _ in range(101)]
num = int(input())
result = 0


for i in range(num):
    a, b = map(int, input().split())
    for j in range(a, a + 10):
        for k in range(b, b + 10):
            paper[k][j] = 1

for i in paper:
    result += sum(i)

print(result)
