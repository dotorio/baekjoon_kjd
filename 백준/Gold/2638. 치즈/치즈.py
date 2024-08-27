dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

time = 0

while True:
    check_arr = [[False]*M for _ in range(N)]
    stack = [(0, 0)]
    check_arr[0][0] = True
    while stack:
        i, j = stack.pop()
        for k in range(4):
            if 0<=i+dx[k]<N and 0<=j+dy[k]<M:
                if not check_arr[i+dx[k]][j+dy[k]] and not arr[i+dx[k]][j+dy[k]]:
                    stack.append((i+dx[k], j+dy[k]))
                    check_arr[i+dx[k]][j+dy[k]] = True
    melt = []
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt = 0
                for k in range(4):
                    if not arr[i+dx[k]][j+dy[k]] and check_arr[i+dx[k]][j+dy[k]]:
                        cnt += 1
                if cnt >= 2:
                    melt.append((i , j))
    if not melt:
        print(time)
        break
    else:
        for i, j in melt:
            arr[i][j] = 0
    time += 1