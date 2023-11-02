import sys

from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
result = []
for i in range(1, n + 1):
    queue.append(i)

target = 1
while queue:

    if target % k == 0:
        result.append(queue.popleft())
        target += 1
    else:
        queue.append(queue.popleft())
        target += 1

print("<", end='')
for i in range(len(result) - 1):
    print("%d, " % result[i], end='')
print(result[-1], end='')
print(">")
