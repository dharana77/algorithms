dx = [0,0,-1,1]
dy = [1,-1,0,0]
visited =[[0]*5 for _ in range(5)]
a=0

def dfs(x, y ,board,ct,mx):
    v = board[x][y]
    global a

    if ct>mx:
        mx= ct
        if mx>a:
            a=mx

    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if nx>=0 and nx<4 and ny>=0 and ny<4:
            if visited[nx][ny]!=1:
                if board[nx][ny]==v:
                    visited[nx][ny]=1
                    dfs(nx,ny,board,ct+1,mx)
                    visited[nx][ny]=0
    if ct>mx:
        mx = ct

def solution(board):
    answer = 0
    global a
    for i in range(4):
        for j in range(4):
            visited[i][j]=1
            mx = dfs(i,j,board,1,0)
            visited[i][j]=0

    if a==1:
        answer = -1
    else:
        answer = a

    return answer