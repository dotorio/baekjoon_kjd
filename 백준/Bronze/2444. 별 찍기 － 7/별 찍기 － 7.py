L = int(input())

for i in range(L):
    print(" " * (L-i-1) + "*" * (2*(i+1)-1))
for i in range(L-1):
    print(" " * (i+1) + "*" * (2*(L-1-i)-1))