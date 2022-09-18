from itertools import combinations_with_replacement

N = int(input()) # 245 -> 256     256의 생성자: 245

for i in range(N+1):
  s = str(i)
  total = i

  for j in s:
    total += int(j)

  if total == N:
    break