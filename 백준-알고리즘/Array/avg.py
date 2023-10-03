n = int(input())
num = 0
result = list(map(int, input().split()))
result.sort()

for i in result:
    num += i / result[n - 1] * 100

print(num / n)
