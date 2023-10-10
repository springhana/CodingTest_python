n = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(stick)):
    if n >= stick[i]:
        count += 1
        n -= stick[i]
    if n == 0:
        break

print(count)