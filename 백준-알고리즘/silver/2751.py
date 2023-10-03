import sys

n = int(input())
result = []
for _ in range(n):
    result.append(int(sys.stdin.readline()))  # sys.stdin.readline()은 prompt message를 인수로 받지 않는다.

result.sort()
for i in result:
    print(i)
