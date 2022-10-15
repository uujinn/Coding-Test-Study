import sys
input = sys.stdin.readline

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

for n in numbers:
  front, back = 0, N-1
  find = False

  while front <= back:
    mid = (front + back) // 2

    if n == A[mid]:
      print(1)
      find = True
      break
    elif n > A[mid]:
      front = mid + 1
    else:
      back = mid - 1
  
  if find == False:
    print(0)