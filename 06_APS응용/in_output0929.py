'''
표준 입출력
1
5 10
0000000000
0123456789
0000000000
0000000000
0000000000
'''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # arr1 = [input() for _ in range(N)]
    # arr2 = [list(map(input()) for _ in range(N))]
    arr = [list(map(int, input())) for _ in range(N)]
    print(arr)
