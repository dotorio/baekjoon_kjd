from itertools import permutations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

for answer in permutations(nums, M):
    print(*answer)