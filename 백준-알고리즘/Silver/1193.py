import sys

n = int(sys.stdin.readline())
# 분자, 분모
a, b = 1, 1

k = 1  # 한 줄에 데이터 갯수
count = 0  # 몇번 연산 했는지 횟수
# 미리 연산 최대 횟수 구하기
while count < n:
    count += k
    k += 1
k -= 1
count -= k  # 라인에 맞게

if k % 2 == 0:
    a = 1
    b = k
    count += 1
    while a != k:
        if count == n:
            break
        a += 1
        b -= 1
        count += 1
else:
    a = k
    b = 1
    count += 1
    while b != k:
        if count == n:
            break
        a -= 1
        b += 1
        count += 1

print(f"{a}/{b}")
