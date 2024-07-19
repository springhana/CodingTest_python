def solution(my_string, indices):
    answer = list(my_string)
    print(answer)
    for i in indices:
        answer[i] = ''
    return ''.join(answer)