N = int(input())
board = [-1]*N
if N%2:
    new_N = N//2+1
    button = True
else:
    new_N = N//2
    button = False
cnt = 0

def place(num):
    global cnt
    if num == N-1:
        if button and new_button:
            cnt += 1
        else:
            cnt += 2
        return
    else:
        for i in range(N):
            board[num+1] = i
            if check(num+1):
                place(num+1)

def check(num):
    for i in range(num):
        if board[i] == board[num] or abs(board[i] - board[num]) == abs(i - num):
            return False
    return True

for i in range(new_N):
    if button and i == new_N-1:
        new_button = True
    else:
        new_button = False
    board[0] = i
    place(0)

print(cnt)