from collections import defaultdict

def solution(record):
    answer = []
    userDB = defaultdict()
    actionDB = []

    for r in record:
        r = r.split()
        if r[0] != 'Leave':
            userDB[r[1]] = r[2]
            actionDB.append((r[0], r[1]))
        else:
            actionDB.append((r[0], r[1]))
    
    for a in actionDB:
        if a[0] == 'Enter':
            s = '들어왔습니다.'
        elif a[0] == 'Leave':
            s = '나갔습니다.'
        else:
            continue
        answer.append(str(userDB[a[1]]) + '님이 ' + s)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))