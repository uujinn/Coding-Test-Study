def solution(dartResult):
    points = {'S': 1, 'D': 2, 'T': 3}
    stack = []
    tmp = ''
    for i in dartResult:
        if i.isnumeric():
            tmp += i
        else:
            if i in points.keys():
                stack.append(int(tmp))
                stack[-1] = stack[-1] ** points[i]
                tmp = ''
            else:
                if i == '*':
                    stack[-1] = stack[-1] * 2
                    if len(stack) > 1:
                        stack[-2] = stack[-2] * 2
                elif i == '#':
                    stack[-1] = -stack[-1]

    return sum(stack)

print(solution('1D2S#10S'))