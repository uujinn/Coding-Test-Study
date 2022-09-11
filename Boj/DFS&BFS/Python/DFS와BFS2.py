from collections import deque
import sys

input = sys.stdin.readline

N, M, V = map(int, input().split())

vertex = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  vertex[a][b] = vertex[b][a] = 1

visited = [0] * (N+1)

def dfs(v):
  visited[v] = 1
  
  print(v, end = ' ')

  for i in range(1, N+1):
    if visited[i] == 0 and vertex[v][i] == 1:
      visited[i] = 1
      dfs(i)

def bfs(v):
  visited[v] = 0
  q = deque()
  q.append(v)
  while q:
    p = q.popleft()
    print(p, end = ' ')
    for i in range(1, N+1):
      if visited[i] == 1 and vertex[i][p] == 1:
        visited[i] = 0
        q.append(i)


dfs(V)
print()
bfs(V)