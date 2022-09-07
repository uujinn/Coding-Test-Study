from itertools import combinations

def solution(nums):
    combs = combinations(nums, 3)
    answer = 0
    for c in combs:

      if isSosu(sum(c)):
        answer += 1
  
    return answer

def isSosu(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True