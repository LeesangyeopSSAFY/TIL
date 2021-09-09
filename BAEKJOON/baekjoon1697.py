# 숨바꼭질
def has(n, k):
    Q = [n]
    while Q:
        val = Q.pop(0)
        if val == k: # 동생의 위치에 도달했을 때
            return num_cnt[val]
        for nv in [val-1, val+1, val*2]: # -1, +1, *2의 경우
            if 0 <= nv <= maxi and num_cnt[nv] == 0: # 도착한 적 없는 위치일 경우, 범위 설정을 안 하면 런타임 에러가 발생한다.
                num_cnt[nv] = num_cnt[val] + 1 # 최소 시간 카운트를 위해
                Q.append(nv)


N, K = map(int, input().split())
maxi = 100000
num_cnt = [0] * (maxi + 1)
print(has(N, K))