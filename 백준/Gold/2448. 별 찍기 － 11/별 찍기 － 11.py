N = int(input())

arr = [[' ']*(2*N-1) for _ in range(N)]

def f(arr, A, B, C, D):
    if B-A == 3:
        for i in range(A, B):
            if i == A:
                arr[i][C+2] = '*'
            elif i == A+1:
                arr[i][C+1] = '*'
                arr[i][C+3] = '*'
            else:
                arr[i][C:D-1] = ['*']*5
        return arr
    else:
        f(arr, A, A+(B-A)//2, C+(D-C)//4, C+(D-C)//4*3)
        f(arr, A+(B-A)//2, B, C, C+(D-C)//2)
        f(arr, A+(B-A)//2, B, C+(D-C)//2, D)
        return arr
                        
f(arr, 0, N, 0, 2*N)
for i in arr:
    print("".join(i))