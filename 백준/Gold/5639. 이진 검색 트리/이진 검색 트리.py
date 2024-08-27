import sys
sys.setrecursionlimit(10**5)

nums = []

while True:
    try:
        nums.append(int(input()))
    except EOFError:
        break
start = 0
tree = dict()
for i in nums:
    if not start:
        start = i
    tree[i] = [0, 0]
    
def create_tree(par, son):
    if par > son:
        if tree[par][0]:
            create_tree(tree[par][0], son)
        else:
            tree[par][0] = son
    else:
        if tree[par][1]:
            create_tree(tree[par][1], son)
        else:
            tree[par][1] = son
        
for i in range(1, len(nums)):
    create_tree(nums[0], nums[i])

def postorder(num):
    if tree[num][0]:
        postorder(tree[num][0])
    if tree[num][1]:
        postorder(tree[num][1])
    print(num)

postorder(nums[0])