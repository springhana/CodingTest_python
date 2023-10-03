max = 0
num = 0
contain = []
for x in range(9):
    a = int(input())
    contain.append(a)

for i in range(len(contain)):
    if max < contain[i]:
        max = contain[i]
        num = i + 1

print(max)
print(num)
