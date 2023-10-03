n = int(input())
result = []
for i in range(n):
    a, b = map(int, input().split())
    result.append("Case #" + str(i + 1) + ": " + str(a) + " + " + str(b) + " = " + str(a + b))

for i in result:
    print(i)
