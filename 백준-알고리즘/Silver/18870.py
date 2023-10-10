import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
new_array = sorted(set(array))
for i in array:
    print(new_array.index(i),end=' ')
