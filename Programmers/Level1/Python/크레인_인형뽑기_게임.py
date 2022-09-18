from collections import deque

def solution(board, moves):
    answer = 0
    q = deque()

    for i in moves:
        for idx in range(len(board)):
            print(len(board))
            if board[idx][i-1] != 0:
                board[idx][i-1] = 0
                if len(q) != 0 and q[-1] == board[idx][i-1]:
                    q.popleft()
                else:
                    q.append(board[idx][i-1])
                break
            else:
                continue
            
    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])