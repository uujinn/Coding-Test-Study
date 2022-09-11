from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())

  arr = list(map(int, input().strip().split()))
  vertex = [[0] * (N+1) for _ in range(N + 1)]
  visited = [0] * (N+1)

  answer = 0

  for idx, i in enumerate(arr):
    vertex[idx+1][i] = 1


  for i in range(1, N+1):
    # bfs
    q = deque()

    if visited[i] == 0:
      q.append(i)
      while q:
        v = q.popleft()
        visited[v] = 1

        for i in range(1, N+1):
          if visited[i] == 0 and vertex[i][v] == 1:
            visited[i] = 1
            q.append(i)

      answer += 1
    else:
      continue
  
  print(answer)


  