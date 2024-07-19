def solution(my_string, queries):
    arr = list(my_string)
    for s, e in queries:
        origin = arr[s:e+1:1]
        arr[s:e+1] = origin[::-1]
    return ''.join(arr)