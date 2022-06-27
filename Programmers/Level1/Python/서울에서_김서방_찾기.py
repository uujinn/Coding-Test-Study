def solution(seoul):
    cnt = 0
    for p in seoul:
        if p == "Kim":
            break
        cnt += 1
    return f'김서방은 {cnt}에 있다'