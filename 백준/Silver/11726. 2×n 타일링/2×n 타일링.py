n = int(input())

a = [0]* n
a[0] = 1
try:
    a[1] = 2
except:
    pass
try:
    for i in range(2, n):
        a[i] = a[i-2]+a[i-1]
except:
    pass
print(a[-1]%10007)