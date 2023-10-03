import sys

result = [0] * 10001

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    result[n] += 1

for i in range(10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)
