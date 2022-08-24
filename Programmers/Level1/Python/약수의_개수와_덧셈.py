def isEven(n):
    if int(n ** 0.5) == (n ** 0.5):
        return False
    else:
        return True

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if isEven(i):
            answer += i
        else:
            answer -= i
    
    return answer