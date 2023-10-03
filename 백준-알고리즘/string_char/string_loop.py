n = int(input())
result = []
for _ in range(n):
    num, text = input().split()
    a = ""
    for i in list(text):
        for _ in range(int(num)):
            a += i
    result.append(a)

for i in result:
    print(i)
