def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        tmp = []
        for idx in range(len(i)):
            tmp.append(i[idx] + j[idx])

        answer.append(tmp)
        
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))