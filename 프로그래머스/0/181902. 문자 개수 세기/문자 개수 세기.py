import string

def solution(my_string):
    aList =[i for i in string.ascii_uppercase]
    
    for i in string.ascii_lowercase:
        aList.append(i)
        
    answer = [0 for i in aList]
    
    for i in range(len(aList)):
        for j in my_string:
            if j == aList[i]:
                answer[i] += 1
    return answer