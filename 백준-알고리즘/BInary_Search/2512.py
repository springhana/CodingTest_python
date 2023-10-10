import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
total_Money = int(sys.stdin.readline())
array.sort()

def binary_search():
    start, end = 0, max(array)
    while start <= end:
        total = 0
        mid = (start + end) // 2
        print(mid)
        for x in array:
            total += min(mid, x)

        # 총 합이 국가예산 보다 클 경우
        if total > total_Money:
            end = mid - 1
        else:
            start = mid + 1
    return end


print(binary_search())
