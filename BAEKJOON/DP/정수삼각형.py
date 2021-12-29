import sys
input = sys.stdin.readline

# def find_ans(r_idx, c_idx, tmp_sum):
#     global ans
#     if r_idx == n:
#         if tmp_sum > ans:
#             ans = tmp_sum
#         return ans
#     find_ans(r_idx+1, c_idx, tmp_sum+triangle[r_idx][c_idx])
#     find_ans(r_idx + 1, c_idx+1, tmp_sum + triangle[r_idx][c_idx])



n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif j == len(triangle[i])-1:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[n-1]))