from collections import deque


def solution(dartResult):
    stack = []
    points = {'S': 1, 'D': 2, 'T': 3}
    tmp = ''
    for i in dartResult:
        if i.isnumeric():
            tmp += i
        elif i in points:
            stack.append(int(tmp) ** points[i])
            tmp = ''
        elif i == '#':
            stack[-1] = stack[-1] * -1
        elif i == '*':
            stack[-1] = stack[-1] * 2
            if len(stack) >= 2:
                stack[-2] = stack[-2] * 2

    return sum(stack)