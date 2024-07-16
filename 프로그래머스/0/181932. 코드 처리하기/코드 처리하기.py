def solution(code):
    answer = []
    mode = 0
    for i in range(len(code)):
        if code[i] == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0
        else:
            if i % 2 == 0:
                if mode == 0:
                    answer.append(code[i])
            else:
                if mode == 1:
                    answer.append(code[i])
                    
    return ''.join(answer) if len(answer) else "EMPTY"