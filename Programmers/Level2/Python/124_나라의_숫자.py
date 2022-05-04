from itertools import product

# 시간 초과 
def solution(n):

    cnt = 1
    num = 1
    while cnt != n:
        for i in product('124', repeat=num):
            p = ''.join(i)
            if cnt == n:
                break
            cnt += 1
        num += 1

    return p

print(solution(4))