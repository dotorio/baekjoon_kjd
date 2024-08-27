N = int(input())

member = []
for _ in range(N):
    member.append(int(input()))

member.sort()
honor, hacker = 1, 0
for i in range(N):
    if i != 0:
        if member[i] != member[i-1]:
            honor += 1
            hacker += member[i] - honor
            member[i] = honor
        else:
            continue
    else:
        hacker += member[i] - honor
        member[i] = honor
print(hacker)