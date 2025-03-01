# https://www.lanqiao.cn/problems/742/learning/
n = int(input())
height_array = []
for i in range(n):
    height_array.append(int(input))


def dynamic_programming():
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            else:
                if dp[j] > dp[i] and height_array[j] < height_array[i]:
                    dp[i] = dp[j] + 1


dp = [0] * n
print(n - max(dp))
