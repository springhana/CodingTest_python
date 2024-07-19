def solution(arr):
    
    if 2 not in arr:
        return [-1]
    else: 
        findArr = list(filter(lambda x: arr[x] == 2, range(len(arr))))
        return arr[findArr[0]:findArr[-1] + 1]
            
