# 184ms
from sys import stdin
from collections import deque


while (True):
    data = stdin.readline().rstrip()
    stack = deque()
    if data == ".":
        break
    for c in data:
        if c == '(' or c == '[':
            stack.append(c)
        elif len(stack) and stack[-1] == '(' and c == ')':
            stack.pop()
        elif len(stack) and stack[-1] == '[' and c == ']':
            stack.pop()
        elif c ==']' or c == ')':
            stack.append(c)
        elif c == '.':
            break
    
    if len(stack) == 0:
        print("yes")
    else:
        print("no")