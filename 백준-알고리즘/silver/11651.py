n = int(input())
result = []

for _ in range(n):
    a, b = map(int, input().split())
    result.append((b, a))

result.sort()
for i in result:
    x, y = i
    print(y, x)
