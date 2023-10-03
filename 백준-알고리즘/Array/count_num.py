n = int(input())

result = list(map(int, input().split()))
count = 0

if len(result) == n:
    a = int(input())
    for i in result:
        if i == a:
            count += 1

print(count)