import sys
input = sys.stdin.readline
N, K, T = map(int, input().split())
shark = sorted(list(map(int, input().split())), reverse=True)
while K >= 1 and shark:
    ori = T
    if shark[0] < T:
        T += sum(shark[:K])
        break
    for i in range(N):
        if shark[i] < T:
            T += shark.pop(i)
            K -= 1
            N -= 1
            break
    if ori == T:
        break
print(T)