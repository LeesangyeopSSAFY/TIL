# 트리 순회

import sys
input = sys.stdin.readline

# 전위 순회
def pre_order(start):
    if start != '.':
        print(start, end='')
        pre_order(tree[start][0])
        pre_order(tree[start][1])

# 중위 순회
def in_order(start):
    if start != '.':
        in_order(tree[start][0])
        print(start, end='')
        in_order(tree[start][1])

# 후위 순회
def post_order(start):
    if start != '.':
        post_order(tree[start][0])
        post_order(tree[start][1])
        print(start, end='')



N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

pre_order('A')
print()
in_order('A')
print()
post_order('A')