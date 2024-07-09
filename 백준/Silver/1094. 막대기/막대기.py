stick = [64, 32, 16, 8, 4, 2, 1]
count = 0
n = int(input())

for i in stick:
    if i <= n:
        n -= i
        count += 1
    if n == 0:
        break

print(count)