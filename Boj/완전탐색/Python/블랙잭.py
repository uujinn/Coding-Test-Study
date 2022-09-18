import sys
from itertools import combinations

input = sys.stdin.readline

N,M = map(int, input().split())
numbers = list(map(int, input().split()))
combs = combinations(numbers, 3)
min_dif = 300000 - 10
answer = 0

for c in combs:
  if abs(sum(c)-M) < min_dif and sum(c) <= M:
    min_dif = abs(sum(c) - M)
    answer = sum(c)
  else:
    continue

print(answer)