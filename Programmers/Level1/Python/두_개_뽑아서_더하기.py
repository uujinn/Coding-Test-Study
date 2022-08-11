from itertools import combinations

def solution(numbers):
    answer = []
    combs = list(combinations(numbers, 2))
    for comb in combs:
        answer.append(sum(comb))
    
    return list(sorted(list(set(answer))))