def getReversed3(n):
    answer = ''

    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)

    return answer

def solution(n):
    return int(getReversed3(n),3)