import sys

from heapq import heappop, heappush

N = int(input())
minHeap, maxHeap = [], []
minNum, maxNum = 1, 0
n = int(sys.stdin.readline())
print(n)
heappush(minHeap, -n)
for _ in range(N-1):
    n = int(sys.stdin.readline())
    mid = heappop(minHeap)
    if -mid > n: # 현재 숫자가 원래 중앙값보다 작을 때
        if minNum > maxNum: # 만약 왼쪽 힙 원소 개수가 더 크다면
            heappush(minHeap, -n) # 현재 숫자는 왼쪽 힙에 넣고
            heappush(maxHeap, -mid) # 원래 중앙값은 오른쪽 힙에 넣는다
            maxNum += 1
        else: # 만약 두 힙 원소 개수가 같다면
            heappush(minHeap, -n) 
            heappush(minHeap, mid) # 현재 숫자, 중앙값 모두 왼쪽 힙에 넣는다
            minNum += 1
    else: # 현재 숫자가 원래 중앙값보다 크거나 같을 때
        if minNum > maxNum: # 만약 왼쪽 힙 원소 개수가 더 크다면
            heappush(minHeap, mid) # 원래 중앙값은 왼쪽 힙에 넣고
            heappush(maxHeap, n) # 현재 숫자는 오른쪽 힙에 넣는다
            maxNum += 1
        else: # 만약 두 힙 원소 개수가 같다면
            rightmid = heappop(maxHeap) # 오른쪽 힙 최소값을 꺼내서
            if rightmid > n: # 만약 오른쪽 힙 최소값이 현재 숫자보다 크다면
                heappush(minHeap, -n) # 현재 숫자를 왼쪽 힙에 넣고
                heappush(minHeap, mid) # 원래 중앙값도 왼쪽 힙에 넣고
                heappush(maxHeap, rightmid) # 오른쪽 힙 최소값을 오른쪽 힙에 넣는다
            else: # 현재 숫자가 오른쪽 힙 최소값 이상이라면
                heappush(minHeap, -rightmid) # 오른쪽 힙 최소값을 왼쪽 힙에 넣고
                heappush(minHeap, mid) # 원래 중앙값도 왼쪽 힙에 넣고
                heappush(maxHeap, n) # 현재 숫자를 오른쪽 힙에 넣는다
            minNum += 1
    mid = heappop(minHeap)
    print(-mid)
    heappush(minHeap, mid)