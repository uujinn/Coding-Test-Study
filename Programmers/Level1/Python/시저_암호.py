def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += ' '
        elif 97 <= ord(c) <= 122:
            dist = n
            if ord(c) + n > 122:
                dist -= 26
            answer += chr(ord(c) + dist)

        elif 65 <= ord(c) <= 90:
            dist = n
            if ord(c) + n > 90:
                dist -= 26
            answer += chr(ord(c) + dist)
    return answer

print(solution("a B z", 4))
