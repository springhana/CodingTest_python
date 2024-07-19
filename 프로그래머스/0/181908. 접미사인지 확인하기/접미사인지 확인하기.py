def solution(my_string, is_suffix):
    answer = 0
    my_suffix = []
    for i in range(len(my_string)):
        my_suffix.append(my_string[i:])
    
    if is_suffix in my_suffix:
        answer = 1
    
    return answer