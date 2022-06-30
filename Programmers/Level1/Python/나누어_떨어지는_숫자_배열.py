def solution(arr, divisor):
    arr = [i for i in arr if i % divisor == 0]
    return sorted(arr) if len(arr)!=0 else [-1]