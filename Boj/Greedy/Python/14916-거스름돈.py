n = int(input())

cnt = 0

while True:
    if n % 5 == 0: # 5의 배수일 경우
        cnt += n // 5
        print(cnt)
        break
    else:
        n -= 2
        cnt += 1
    
    if n < 0:
        print(-1)
        break

