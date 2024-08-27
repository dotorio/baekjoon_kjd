from heapq import heappop, heappush

n, m, r = map(int, input().split())

items = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(start):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heappop(pq)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(pq, (distance, neighbor))
    
    return distances

max_item = 0

for i in range(1, n+1):
    distances = dijkstra(i)
    current_item_count = 0
    for j in range(1, n+1):
        if distances[j] <= m:
            current_item_count += items[j]
    max_item = max(max_item, current_item_count)

print(max_item)
