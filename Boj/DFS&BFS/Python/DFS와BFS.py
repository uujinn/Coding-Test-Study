from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input())
vertex = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  vertex[a][b] = vertex[b][a] = 1
visited = [0] * (n+1)

def dfs(v):
  visited[v] = 1
  print(v, end = ' ')
  for i in range(1, n+1):
    if visited[i] == 0 and vertex[v][i] == 1:
      dfs(i)
  
def bfs(v):
  visited[v] = 0
  q = deque()
  q.append(v)

  while q:
    point = q.popleft()
    print(point, end = ' ')
    if visited[point] == 1 and vertex[v][i] == 1:
      visited[point] = 0
      q.append(i)

dfs(v)
print()
bfs(v)