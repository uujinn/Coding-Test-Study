import sys

input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().split())
check = [0] * (9*5+9*5+9*5+9*5+9*5)

def cal(n, m):
  a = str(n)
  answer = 0
  for i in a:
    answer += pow(int(i), m)
  return answer

def dfs(n, m, count, check):
  if check[n] != 0:
    return check[n]-1
  check[n] = count
  b = cal(n, m)
  count += 1
  return dfs(b, m, count, check)

count = 1
print(dfs(N, M, count, check))