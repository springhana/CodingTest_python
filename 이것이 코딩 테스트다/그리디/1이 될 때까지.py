n, m = map(int, input().split())
result = 0

# 내가 푼 방법
while True:
    if n == 1:
        break
    if n % m == 0:
        n //= m
        result += 1
    else:
        n -= 1
        result += 1
print(result)

# 책 방법
while n >= m:  # n이상이라면 m로 계속 나누기
    while n % m != 0:
        n -= 1
        result += 1
    n //= m
    result += 1

while n > 1:
    n -= 1
    result += 1
print(result)

# 숫자가 클 경우 빠른 방법
while True:
    target = (n // m) * m
    result += (n - target)
    if n < m:
        break
    result += 1
    n //= m
result += (n - 1)
print(result)
