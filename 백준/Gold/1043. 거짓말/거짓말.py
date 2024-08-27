N, M = map(int, input().split())

member = [True]*(N+1)
can_lie_party = [True]*M
lie_cnt, *lie_mem = map(int, input().split())
parties = dict()
mem_to_party = dict()
for i in range(1, N+1):
    mem_to_party[i] = []

for i in range(M):
    par_cnt, *party = map(int, input().split())
    parties[i] = party
    for j in party:
        mem_to_party[j].append(i)
max_party = 0
for now_mem in lie_mem:
    member[now_mem] = False
    for par in mem_to_party[now_mem]:
        can_lie_party[par] = False
        for mem in parties[par]:
            if mem not in lie_mem:
                lie_mem.append(mem)
print(can_lie_party.count(True))

    
