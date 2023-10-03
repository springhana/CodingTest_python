a, b = map(int, input().split())

result = list(map(int, input().split()))
num = []

if len(result) == a:
    for i in result:
        if i < b:
            num.append(i)

for i in num:
    print(i,end=' ')
