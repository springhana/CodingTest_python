# 가지고 있는 부품
n = int(input())
part_n = list(map(int, input().split()))
part_n.sort()

# 손님이 제시한 부품
m = int(input())
part_m = list(map(int, input().split()))


def binary_search(target, start, end):
    if start >= end:
        return "no"
    mid = (start + end) // 2

    if part_n[mid] == target:
        return "yes"
    elif part_n[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)


for i in range(m):
    result = binary_search(part_m[i], 0, n - 1)
    print(result, end=' ')
