from itertools import combinations

def solution(d, budget):
    d.sort()
    for i in range(len(d), -1, -1):
        if sum(d[:i]) <= budget:
            return i