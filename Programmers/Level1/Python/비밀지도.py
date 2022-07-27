def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bin_arr = bin(arr1[i] | arr2[i])[2:]
        answer.append(("0" * (n-len(bin_arr)) + bin_arr).replace("1", "#").replace("0", " "))

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))