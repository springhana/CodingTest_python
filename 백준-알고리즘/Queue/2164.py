from collections import deque

n = int(input())
queue = deque()

for i in range(1, n + 1):
    queue.append(i)

target = 1
while len(queue) != 1:
    queue.popleft()
    target += 1

    a = queue.popleft()
    queue.append(a)
    target += 1

print(queue[0])