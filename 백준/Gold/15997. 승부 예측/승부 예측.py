A, B, C, D = input().split()
match = []
for _ in range(6):
    X, Y, W, Dr, L = input().split()
    match.append((X, Y, float(W), float(Dr), float(L)))
rate = {A: 0, B: 0, C: 0, D: 0}
cal = {A: 0, B: 0, C: 0, D: 0, 'per':1}

def f(idx, cal):
    global rate
    if idx == 6:
        result = []
        for i in cal:
            if i == 'per':
                break
            result.append((cal[i], i))
        result.sort(reverse=True)
        rank = dict()
        rank_now = 1
        ctn = 0
        one, two = 1, 0
        for i in range(4):
            if not i:
                rank[result[i][1]] = rank_now
            else:
                if result[i-1][0] != result[i][0]:
                    rank_now += 1 + ctn
                    ctn = 0
                else:
                    ctn += 1
                rank[result[i][1]] = rank_now
                if rank_now == 1:
                    one += 1
                elif rank_now == 2:
                    two += 1
        for i in rank:
            if rank[i] == 1:
                if one > 2:
                    rate[i] += cal['per'] / one * 2
                else:
                    rate[i] += cal['per']
            elif rank[i] == 2:
                rate[i] += cal['per'] / two
    else:
        if match[idx][2]:
            cal[match[idx][0]] += 3
            cal['per'] *= match[idx][2]
            f(idx+1, cal)
            cal[match[idx][0]] -= 3
            cal['per'] /= match[idx][2]
        if match[idx][3]:
            cal[match[idx][0]] += 1
            cal[match[idx][1]] += 1
            cal['per'] *= match[idx][3]
            f(idx+1, cal)
            cal[match[idx][0]] -= 1
            cal[match[idx][1]] -= 1
            cal['per'] /= match[idx][3]
        if match[idx][4]:
            cal[match[idx][1]] += 3
            cal['per'] *= match[idx][4]
            f(idx+1, cal)
            cal[match[idx][1]] -= 3
            cal['per'] /= match[idx][4]

f(0, cal)

for i in rate:
    print(rate[i])