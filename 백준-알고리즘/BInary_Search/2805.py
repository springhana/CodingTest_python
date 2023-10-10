n, m = map(int, input().split())
array = list(map(int, input().split()))


def binary_search(start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for x in array:
            if x > mid:
                total += x - mid

        # 목표가 총 양보다 적을 경우
        if total >= m:
            result = mid
            start = mid + 1
        # 목표가 총 양보다 많을 경우
        else:
            end = mid - 1
    return result


print(binary_search(0, max(array)))
