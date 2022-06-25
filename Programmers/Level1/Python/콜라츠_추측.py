def solution(n):
    answer = 0

    if n == 1:
        return 0
        
    while (n!=1):
        if answer == 500:
            print(-1)

        if n % 2 == 0:
            n /= 2

        else:
            n /= 3
            n += 1
        answer += 1

    return answer