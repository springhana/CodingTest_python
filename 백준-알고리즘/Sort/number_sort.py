n = int(input())
result = []
for _ in range(n):
    num = int(input())
    result.append(num)

result.sort()
for i in result:
    print(i)
