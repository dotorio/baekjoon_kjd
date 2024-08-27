import sys
input = sys.stdin.readline

from heapq import heappop, heappush

N, M = map(int, input().split())

nodes = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for _ in range(M):
    s, e, l = map(int, input().split())
    if nodes[s] and s != N-1:
        continue
    elif nodes[e] and e != N-1:
        continue
    else:
        graph[s].append((e, l))
        graph[e].append((s, l))

pq = []
heappush(pq, (0, 0))

visited = [False] * N

while pq:
    time, now = heappop(pq)
    if now == N-1:
        print(time)
        break
    if visited[now]:
        continue
    visited[now] = True
    for node, go in graph[now]:
        if not visited[node]:
            heappush(pq, (time + go, node))
else:
    print(-1)