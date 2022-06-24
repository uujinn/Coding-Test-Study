def solution(x):
    sum_x = sum(map(int, list(str(x))))
    print(sum_x)
    if x % sum_x == 0:
        return True
    else:
        return False
    
    
print(solution(10))