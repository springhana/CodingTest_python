import sys

word = list(sys.stdin.readline().strip())
bomb = list(sys.stdin.readline().strip())
stack = []
for i in word:
    stack.append(i)
    if stack[len(stack) - len(bomb):len(stack)] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(*stack,sep='')
else:
    print("FRULA")
