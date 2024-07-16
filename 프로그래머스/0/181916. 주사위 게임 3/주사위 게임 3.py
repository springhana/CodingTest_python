def solution(a, b, c, d):
    answer = 0
    origin = [a, b, c, d]
    arr = list(set(origin))
    
    if len(arr) == 4:
        answer = min(arr)
    elif len(arr) == 3:
        max_num = max(origin, key=origin.count)
        tmp = [num for num in arr if num != max_num]
        answer = tmp[0] * tmp[1]
    elif len(arr) == 2:
        if max([origin.count(num) for num in arr]) > 2:
            max_num = max(origin, key=origin.count)
            min_num = min(origin, key=origin.count)
            answer = ((10 * max_num + min_num) ** 2)
        else:
            answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1]))
    elif len(arr) == 1:
            answer = int(str(arr[0]) * 4)
    return answer
