string = list(input())
explode = list(input())
idx_stack = []
stack = []
len_ex, len_str = len(explode), len(string)
idx, i = 0, 0
while i != len_str:
    stack.append(string[i])
    if string[i] == explode[idx]:
        i += 1
        idx += 1
        if idx == len_ex:
            del stack[-len_ex:]
            if not idx_stack:
                idx = 0
            else:
                idx = idx_stack.pop()
    else:
        i += 1
        if idx:
            idx_stack.append(idx)
            idx = 0
            stack.pop()
            i -= 1
        else:
            idx_stack.append(0)
if stack:
    print(''.join(stack))
else:
    print('FRULA')
