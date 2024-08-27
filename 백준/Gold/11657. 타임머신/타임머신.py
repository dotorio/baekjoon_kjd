
from collections import deque

# 입력 받기
N, M = map(int, input().split())
edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

# 벨만-포드 알고리즘
def bellman_ford(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0

    # N-1번 모든 간선 완화
    for i in range(N - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # 음수 사이클 검사
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return False, []

    return True, dist

# 시작 노드는 1
success, distances = bellman_ford(1)

if not success:
    print(-1)
else:
    for i in range(2, N + 1):
        if distances[i] == float('inf'):
            print(-1)
        else:
            print(distances[i])
