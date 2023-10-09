n = input()
x = int(n[1])
y = int(ord(n[0])) - int(ord("a")) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0

for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if next_x > 0 and next_y > 0 and next_x < 9 and next_y < 9:
        result += 1

print(result)
