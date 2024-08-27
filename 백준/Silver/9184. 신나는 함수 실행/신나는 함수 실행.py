dp = [[[0]*21 for i in range(21)] for j in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if not i or not j or not k:
                dp[i][j][k] = 1
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i<j and j<k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]

def f(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return f'w({a}, {b}, {c}) = {dp[0][0][0]}'
    elif a > 20 or b > 20 or c > 20:
        return f'w({a}, {b}, {c}) = {dp[20][20][20]}'
    return f'w({a}, {b}, {c}) = {dp[a][b][c]}'

while True:
    a, b, c = map(int, input().split())
    if (a,b,c) == (-1, -1, -1):
        break
    print(f(a,b,c))