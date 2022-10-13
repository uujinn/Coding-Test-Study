def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 1단계
    # 2단계
    for i in new_id:
        if i.isalnum() or (i=='-' or i == '_' or i == '.'):
            answer += i
    new_id = answer
    
    # 3단계
    while True:
        if '..' in new_id:
            new_id = new_id.replace('..', '.')
        else:
            break
    
    # 4 & 5단계
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id == '':
        new_id += 'a'
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7단계
    if len(new_id) <= 2:
        while True:
            if len(new_id) == 3:
                break
            new_id += new_id[-1]
    
    return new_id

print(solution("=.="))
