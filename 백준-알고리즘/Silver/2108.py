import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

# 평균
print(round(sum(array) / n))

# 중앙값
print(array[n // 2])

# 최빈값
index = [0] * (array[n - 1] - array[0] + 1)
for i in range(n):
    index[array[i] - array[0]] += 1
count = 0
for i in range(len(index)):
    if index[i] == max(index):
        if count == 1:
            index[i] = index[i] + 1
        else:
            count += 1
if n <= 1:
    print(array[0])
else:
    if max(index) <= 2:
        print(array[1])
    else:
        # print(sorted(list(set(array)))[index.index(max(index))])
        print(index.index(max(index)) + min(array))

# 범위
print(max(array) - min(array))
