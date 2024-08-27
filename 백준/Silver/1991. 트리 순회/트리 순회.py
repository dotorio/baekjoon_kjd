left, right = dict(), dict()
N = int(input())
for _ in range(N):
    par, left_son, right_son = input().split()
    if left_son != '.':
        left[par] = left_son
    if right_son != '.':
        right[par] = right_son

def tree(char):
    preorder, inorder, postorder = [], [], []
    preorder.append(char)
    if char in left:
        next_preorder, next_inorder, next_postorder = tree(left[char])
        preorder.extend(next_preorder)
        inorder.extend(next_inorder)
        postorder.extend(next_postorder)
    inorder.append(char)
    if char in right:
        next_preorder, next_inorder, next_postorder = tree(right[char])
        preorder.extend(next_preorder)
        inorder.extend(next_inorder)
        postorder.extend(next_postorder)
    postorder.append(char)
    return preorder, inorder, postorder

preorder, inorder, postorder = tree('A')

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))
