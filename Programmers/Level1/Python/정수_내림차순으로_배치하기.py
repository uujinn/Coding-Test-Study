def solution(n):
    answer = 0
    answer = sorted(map(int, (list(str(n))), reverse=True))
    return answer