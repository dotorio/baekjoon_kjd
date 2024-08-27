N, K = map(int, input().split())
a = 1
b = 1
for i in range(K):
    a *= N-i
for i in range(K-1):
    b *= K-i
print(int(a/b))