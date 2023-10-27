import sys

n = sys.stdin.readline()
wait = list(map(int, sys.stdin.readline().split()))
temp = []
target = 1

for i in wait:
    temp.append(i)
    while temp and temp[-1] == target:
        temp.pop()
        target += 1
    if len(temp) > 1 and temp[-1] > temp[-2]:
        print("Sad")
        sys.exit()

if temp:
    print("Sad")
else:
    print("Nice")

# 1. 순차적으로 실행
# 2. temp에서 [-1] 값이 [-2]보다 크면 안됨
