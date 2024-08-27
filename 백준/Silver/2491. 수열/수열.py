N = int(input())
seq = list(map(int, input().split()))
max_length = 1
i = 0
while i < N:
    seq_length = 1
    while i+1 < N and seq[i] <= seq[i+1]:
        seq_length += 1
        i = i+1
    max_length = max(max_length, seq_length)
    i = i+1
i = 0
while i < N:
    seq_length = 1
    while i+1 < N and seq[i] >= seq[i+1]:
        seq_length += 1
        i = i+1
    max_length = max(max_length, seq_length)
    i = i+1
print(max_length)