def merge_sort(M):
    if len(M) == 1:
        return M

    mid = len(M) // 2
    left = M[:mid]
    right = M[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global ans2
    result = [0] * (len(left) + len(right))
    idx = len(result) - 1
    L = len(left) - 1
    R = len(right) - 1
    # 왼쪽 마지막 값이 오른쪽 마지막 값보다 크다면
    if left[L] > right[R]:
        ans2 += 1

    while L >= 0 and R >= 0:
        if left[L] > right[R]:
            result[idx] = left[L]
            L -= 1
            idx -= 1
        else:
            result[idx] = right[R]
            R -= 1
            idx -= 1
    while L >= 0:
        result[idx] = left[L]
        L -= 1
        idx -= 1
    while R >= 0:
        result[idx] = right[R]
        R -= 1
        idx -= 1

    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # ans2: 오른쪽 원소가 먼저 복사되는 경우의 수
    ans2 = 0
    ans = merge_sort(arr)
    # ans1: 병합 정렬 후 N//2번째 원소
    ans1 = ans[N//2]
    print('#{} {} {}'.format(t, ans1, ans2))