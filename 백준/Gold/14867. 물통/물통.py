from collections import deque

a, b, c, d = map(int, input().split())
past = dict()
coms = deque()
past[(0, 0)] = True
coms.append((0, 0, 0))

def g(x, y, cnt):
    global past, coms
    try:
        if past[(x,y)]:
            return False
    except:
        past[(x,y)] = True
        coms.append((x, y, cnt+1))
        return True
    
def check(x, y, cnt):
    if (x, y) == (c, d):
        print(cnt + 1)
        return True

if (c, d) == (0, 0):
    print(0)
else:    
    while coms:       
        x, y, cnt = coms.popleft()
        if x < a and g(a, y, cnt):
            if check(a, y, cnt):
                break
        if y < b and g(x, b, cnt):
            if check(x, b, cnt):
                break
        if 0 < x and g(0, y, cnt):
            if check(0, y, cnt):
                break
        if 0 < y and g(x, 0, cnt):
            if check(x, 0, cnt):
                break
        if 0 < x and y < b:
            ty = min(b, x+y)
            tx = x - (ty - y)
            if g(tx, ty, cnt):
                if check(tx, ty, cnt):
                    break
        if 0 < y and x < a:
            tx = min(a, x+y)
            ty = y - (tx - x)
            if g(tx, ty, cnt):
                if check(tx, ty, cnt):
                    break
    else:
        print(-1)
            
        
        
            