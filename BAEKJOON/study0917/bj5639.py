import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def BST(st, ed):
    if st > ed:
        return
    
    now = ed + 1
    for i in range(st+1, ed+1):
        if tree[st] < tree[i]:
            now = i
            break
    
    BST(st+1, now-1)
    BST(now, ed)
    print(tree[st])

tree = []
cnt = 0
while cnt <= 10000:
    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    cnt += 1

BST(0, len(tree) -1)

