from itertools import combinations

def solution(d, budget):
    for i in range(len(d), 0, -1):
        combs = list(combinations(d, i))
        for comb in combs:
            if sum(comb) <= budget:
                return i
    return 0