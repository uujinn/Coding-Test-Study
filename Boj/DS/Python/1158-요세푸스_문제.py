from collections import deque
from sys import stdin

N, K = map(int, stdin.readline().split())

queue = deque()
answer = []

for i in range(N):
    queue.append(i+1)


for _ in range(N):
    queue.rotate(-K)
    answer.append(queue.pop())
    
print("<" + str(", ".join(map(str, answer)))+ ">")