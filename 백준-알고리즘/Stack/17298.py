import sys

# n = int(sys.stdin.readline())
# array = list(map(int, sys.stdin.readline().split()))
# stack = array[1:n]
#
# target = 0
#
# while target != n:
#     answer = 0
#     for i in stack:
#         if array[target] < i:
#             print(i)
#             stack = stack[1:len(stack)]
#             answer = 1
#             break
#     if answer == 0:
#         print(-1)
#     target += 1


input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

NGE = [-1] * n
stack = []

for i in range(n):
    while stack and array[stack[-1]] < array[i]:
        NGE[stack.pop()] = array[i]
    stack.append(i)

print(*NGE)
