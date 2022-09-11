from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque()
  q.append((0, 0))

  while q:
    a, b = q.popleft()
    
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[a][b] + 1
          q.append((nx, ny))
    
  print(graph[N-1][M-1])

bfs()
