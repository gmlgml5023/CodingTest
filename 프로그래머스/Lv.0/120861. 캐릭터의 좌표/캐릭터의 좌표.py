def solution(keyinput, board):
    answer = [0,0]
    limit_x, limit_y = board[0]//2, board[1]//2

    for input in keyinput:
        if (input == 'up')&(answer[1]<limit_y):
            answer[1]+=1
        elif (input == 'down')&(answer[1]>-limit_y):
            answer[1]-=1
        elif (input == 'right')&(answer[0]<limit_x):
            answer[0]+=1
        elif (input == 'left')&(answer[0]>-limit_x):
            answer[0]-=1
    return answer

def solution2(keyinput, board):
    x_lim,y_lim = board[0]//2,board[1]//2
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    x,y = 0,0
    for k in keyinput:
        dx,dy = move[k]
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            x,y = x+dx,y+dy
    return [x,y]