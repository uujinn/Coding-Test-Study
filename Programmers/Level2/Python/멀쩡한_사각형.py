def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(w,h):
    answer = w * h - (w + h - gcd(w, h))

    return answer