# 이진 검색 트리
# 이 문제는 잘 몰라서 찾아봤습니다
# 이론은 이해가 어느 정도 가는데 코드는 아직 제대로 모르겠습니다
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

