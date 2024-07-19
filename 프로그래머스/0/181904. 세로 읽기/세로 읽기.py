import math

def solution(my_string, m, c):
    answer = ''
    arr = []
    for i in range(math.ceil(len(my_string) // m)):
        arr.append(list(my_string[i * m: i * m + m]))
    
    for i in arr:
        answer += i[c-1]
    return answer