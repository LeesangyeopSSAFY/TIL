def solution(progresses, speeds):
    answer = []
    while progresses:
        if progresses[0] >= 100:
            cnt = 0
            for tmp in progresses:
                if tmp >= 100:
                    cnt += 1
                else:
                    break
            for i in range(cnt):
                progresses.pop(0)
                speeds.pop(0)
            answer.append(cnt)
        for idx in range(len(speeds)):
            progresses[idx] += speeds[idx]
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))

