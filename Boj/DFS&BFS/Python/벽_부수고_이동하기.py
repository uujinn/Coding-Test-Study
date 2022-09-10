from collections import deque

N, M = map(int, input().split())

graph = []

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

for _ in range(N):
  graph.append(list(map(int, list(map(int, input())))))

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, w):
  q = deque()
  q.append(x, y, w)

  while q:
    a, b, c = q.popleft()

    if a == N - 1 and b == M - 1:
      return visited[a][b][c]

    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M :
        continue

      if graph[nx][ny] == 1 and c == 0:
        visited[nx][ny][1] = visited[a][b][0] + 1
        q.append((nx, ny, 1))
      elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
        visited[nx][ny][c] = visited[x][y][c] + 1
        q.append((nx, ny , c))

  return -1

print(bfs(0,0,0))
