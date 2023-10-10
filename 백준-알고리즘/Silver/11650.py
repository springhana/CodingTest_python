n = int(input())
result = []

for _ in range(n):
    a, b = map(int, input().split())
    result.append((a, b))
result.sort()
for i in result:
    x, y = i
    print(x, y)
