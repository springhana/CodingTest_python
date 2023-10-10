# N 아파트 단지의 수, K 통학버스의 정원, S 학교의 위치
from collections import deque

N, K, S = map(int, input().split())
left, right = deque(), deque()

for _ in range(N):
    # 아파트 위치, 학생 수
    a, b = map(int, input().split())
    if a > S:
        right.append((a - S, b))  # 학교보다 오른쪽에 있다면, (단지 위치 - 학교 위치, 학생 수)
    else:
        left.append((S - a, b))  # 학교보다 왼쪽에 있다면, (학교 위치 - 단지 위치, 학생 수)

left = sorted(left, key=lambda x: x[0])
right = sorted(right, key=lambda x: x[0])

answer = 0
while left:
    remain, distance = K, 0
    # 버스에 K만큼 1번
    while remain > 0 and left:
        a = left.pop()
        print("왼쪽: ", a)
        if remain >= a[1]:
            remain -= a[1]
        else:
            left.append((a[0], a[1] - remain))
            remain = 0
        distance = max(distance, a[0])
    answer += distance * 2

while right:
    remain, distance = K, 0
    # 버스에 K만큼 1번
    while remain > 0 and right:
        a = right.pop()
        print("오른쪽: ", a)
        if remain >= a[1]:
            remain -= a[1]
        else:
            right.append((a[0], a[1] - remain))
            remain = 0
        distance = max(distance, a[0])
    answer += distance * 2

print(answer)
