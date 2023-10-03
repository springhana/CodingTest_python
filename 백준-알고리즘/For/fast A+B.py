import sys

n = int(sys.stdin.readline().rstrip())
result = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a + b)

for i in result:
    print(i)
