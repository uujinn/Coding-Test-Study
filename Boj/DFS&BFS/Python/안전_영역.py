import sys
sys.setrecursionlimit(10**9)


n = int(input())
graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * (n) for _ in range(n)]
cnt = 0
answer = []

def dfs(x, y, height):
  visited[x][y] = 1
  
  global cnt
  cnt += 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < n:
      if visited[nx][ny] == 0 and graph[nx][ny] > (height+1):
        visited[nx][ny] = 1
        cnt += 1
        dfs(nx, ny, height)

  if cnt >= 1:
    return 1
  else:
    return 0

for height in range(-1, max(max(graph))+1):
  visited = [[0] * (n) for _ in range(n)]
  tmp = 0
  cnt = 0
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0 and graph[i][j] > (height+1):
        tmp += dfs(i, j, height) 
  # print(answer)
  answer.append(tmp)

print(max(answer) if len(answer) > 0 else 0)
