n = input()
result = []
for i in n:
    result.append(i)

for j in sorted(result, reverse=True):
    print(j, end='')
