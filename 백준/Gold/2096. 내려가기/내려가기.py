N = int(input())
arr = [[0,0]]*3
for j in range(N):
    nums = list(map(int, input().split()))
    new_arr = [[0,0] for _ in range(3)] 
    if j == 0:
        for i in range(3):
            new_arr[i] = [nums[i], nums[i]]
    else:    
        new_arr[0][0] = max(arr[0][0], arr[1][0]) + nums[0]

        new_arr[0][1] = min(arr[0][1], arr[1][1]) + nums[0]

        new_arr[1][0] = max(arr[0][0], arr[1][0], arr[2][0]) + nums[1]

        new_arr[1][1] = min(arr[0][1], arr[1][1], arr[2][1]) + nums[1]

        new_arr[2][0] = max(arr[1][0], arr[2][0]) + nums[2]

        new_arr[2][1] = min(arr[1][1], arr[2][1]) + nums[2]
 
    arr = new_arr
max_score = 0
min_score = 10**10
for i in range(3):
    max_score = max(max_score, arr[i][0])
    min_score = min(min_score, arr[i][1])
print(max_score, min_score)