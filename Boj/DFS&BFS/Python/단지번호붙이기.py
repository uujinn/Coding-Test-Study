from collections import deque

n = int(input())
maps = []

for _ in range(n):
  maps.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
  queue = deque()
  queue.append((a, b))

  tmp = 0

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or ny < 0 or nx >= n or ny >= n:
          continue

      if maps[nx][ny] == 1:
        tmp += 1
        maps[nx][ny] = 0
        queue.append((nx, ny))

  if tmp == 0:
    tmp = 1
  return tmp

# main
answer = []
for i in range(n):
  for j in range(n):
    if maps[i][j] == 1:
      answer.append(bfs(i, j))

print(len(answer))
answer.sort()

for i in answer:
  print(i)
