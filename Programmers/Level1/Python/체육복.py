def solution(n, lost, reserve):
    answer = 0
    students = [1] * n 

    for i in range(n):
        if (i+1) in lost:
            students[i] -= 1
        if (i+1) in reserve:
            students[i] += 1
         
    for i in range(n):
        if i != len(students)-1:
            if students[i] > 1 and students[i+1] == 0:
                students[i] -= 1
                students[i+1] += 1
            if i != 0:
                if students[i] > 1 and students[i-1] == 0:
                    students[i] -= 1
                    students[i-1] += 1
                
    
    for i in students:
        if i > 0:
            answer += 1
    return answer