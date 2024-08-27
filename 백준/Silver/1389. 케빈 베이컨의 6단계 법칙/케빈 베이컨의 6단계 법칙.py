from copy import deepcopy

N, M = map(int, input().split())
graph = [set() for _ in range(N+1)]
visited = [[False]*(N+1) for _ in range(N+1)]
finish = set(range(1, N+1))
nums = [0]*(N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].add(B)
    graph[B].add(A)

min_cnt = 10**5

def f(i, nodes, brg, cnt):
    global visited, nums, min_cnt
    new_go = set()
    for node in nodes:
        if not visited[i][node]:
            visited[i][node] = True
            cnt += brg
            new_go |= graph[node]
    if new_go:
        nodes |= new_go
        return f(i, nodes, brg+1, cnt)
    nums[i] = cnt
    min_cnt = min(min_cnt, cnt)
    return

        

for i in range(1, N+1):
    f(i, deepcopy(graph[i]), 1, 0)

for i in range(1, N+1):
    if nums[i] == min_cnt:
        print(i)
        break