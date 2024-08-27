N = int(input())
map = list(list(map(int, input())) for _ in range(N))
map2 = list([False] * N for _ in range(N))
con = {}
for j in range(N):
    for i in range(N):
        con[(j, i)] = []
for j in range(N):
    for i in range(N):
        if map[j][i] == 1:
            if i-1 >= 0 and map[j][i-1] == 1:
                con[(j, i)].append([j, i-1])
            if j-1 >= 0 and map[j-1][i] == 1:
                con[(j, i)].append([j-1, i])
            if i+1 <= N-1 and map[j][i+1] == 1:
                con[(j, i)].append([j, i+1])
            if j+1 <= N-1 and map[j+1][i] == 1:
                con[(j, i)].append([j+1, i])
dangi_cnt = 0
cnt = []
for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and map2[j][i] == False:
            stack = []
            stack.extend(con[(j, i)])
            this_dangi = 1
            map2[j][i] = True
            while stack:
                now = stack.pop()
                if map2[now[0]][now[1]] == False:
                    map2[now[0]][now[1]] = True
                    stack.extend(con[(now[0], now[1])])
                    this_dangi += 1
            dangi_cnt += 1
            cnt.append(this_dangi)
print(dangi_cnt)
cnt.sort()
for i in cnt:
    print(i)