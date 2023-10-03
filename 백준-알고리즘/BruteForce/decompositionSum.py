n = int(input())
result = n
for i in range(1, n):
    number = 0
    for j in str(i):
        number += int(j)
    number += i
    if number == n:
        result = min(i, result)
if result != n:
    print(result)
else:
    print(0)
