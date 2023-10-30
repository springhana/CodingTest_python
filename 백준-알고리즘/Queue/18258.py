import sys
from collections import deque

n = int(input())

queue = deque()
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    cmd = word[0:5].strip()
    if cmd == "push":
        queue.append(word[5:])
    elif cmd == "pop":
        if queue:
            a = queue.popleft()
            print(a)
        else:
            print(-1)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
