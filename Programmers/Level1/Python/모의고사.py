def solution(answers):
    
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer = [0] * 4
        
    for idx, a in enumerate(answers):
        if a == one[idx % len(one)]:
            answer[1] += 1
        if a == two[idx % len(two)]:
            answer[2] += 1
        if a == three[idx % len(three)]:
            answer[3] += 1
    
    max_value = max(answer)

    
    return list(filter(lambda x: answer[x] == max_value, range(len(answer))))