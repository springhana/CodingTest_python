import sys

sys.setrecursionlimit(1000000000)

n = int(input())
array = []

for i in range(n):
    array.append(int(input()))


# array = sorted(array, reverse=True)
# print(array)


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개 인 경우
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
