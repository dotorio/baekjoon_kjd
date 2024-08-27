from itertools import permutations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))


answer = sorted(list(set(permutations(nums, M))))


for i in answer:
    print(*i)