def solution(my_string, is_prefix):
    answer = 0
    my_prefix = []
    for i in range(len(my_string)):
        my_prefix.append(my_string[:i])
    
    if is_prefix in my_prefix:
        answer = 1
        
    return answer