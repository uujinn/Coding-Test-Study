import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input())

def dfs(v):
  visited[v] = 1
  n = vertex[v]

  if visited[n] == 0:
    dfs(n)

for _ in range(T):
  N = int(input())

  arr = list(map(int, input().strip().split()))
  vertex = [0] * (N+1)
  visited = [0] * (N+1)

  answer = 0

  for idx, i in enumerate(arr):
    vertex[idx+1] = i

  for i in range(1, N+1):
    if visited[i] == 0:
      dfs(i)
      answer += 1

  print(answer)

