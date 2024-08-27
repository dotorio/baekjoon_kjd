from itertools import permutations

N, K = map(int, input().split())
kits = list(map(int, input().split()))
result = 0
for routine in list(permutations(kits, N)):
    start = 0
    for kit in routine:
        start += kit - K
        if start < 0:
            break
    else:
        result += 1
print(result)