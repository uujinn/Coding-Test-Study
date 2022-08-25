def solution(N, stages):
    answer = []
    
    for i in range(1, N+1):
        up_players = 0
        down_players = 0
        for stage in stages:
            if stage == i: 
                up_players += 1
                down_players += 1
            elif stage > i: down_players += 1
        
        if down_players == 0: failure = 0
        else: failure = up_players/down_players
        
        answer.append([i, failure])
        answer.sort(key=lambda x: (-x[1], x[0]))

    return [i[0] for i in answer]