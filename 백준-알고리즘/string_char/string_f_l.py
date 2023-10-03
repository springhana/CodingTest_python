m = int(input())
list = []
for _ in range(m):
    n = input()
    list.append(n.strip()[0]+n.strip()[-1])

for i in list:
    print(i)