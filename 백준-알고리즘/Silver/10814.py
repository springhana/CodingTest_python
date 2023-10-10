n = int(input())
result = []
for i in range(n):
    old, name = map(str, input().split())
    result.append((int(old), i, name))

m = sorted(result)
for i in m:
    old, num, name = i
    print(old, name)
