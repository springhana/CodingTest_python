n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += data[n - 1]
        m -= 1
    if m == 0:
        break
    result += data[n - 2]
    m -= 1

print(result)

# 규칙을 사용한 방법
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
# data.sort()
# result = 0
#
# count = int(m / (k + 1)) * k  # 가장 큰 수 횟수
# count += m % (k + 1)  # 두번째 큰 수  더하는 횟수
#
# result += count * data[n - 1]
# result += (m - count) * data[n - 2]
#
# print(result)
