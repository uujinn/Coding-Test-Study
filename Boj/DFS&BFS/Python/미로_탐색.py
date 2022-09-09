from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    v = queue.popleft()

    for i in range(4):
      nx = v[0] + dx[i]
      ny = v[1] + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

      if graph[nx][ny] == 0:
        continue
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[v[0]][v[1]] + 1
        queue.append((nx, ny))
    
  return graph[n-1][m-1]

print(bfs(0, 0))