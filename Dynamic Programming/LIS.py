# https://www.lanqiao.cn/problems/742/learning/
n = int(input())
height_array = list((map(int, input().split())))


def dynamic_programming():
    for i in range(1, n):
        for j in range(i):
            if dp[j] + 1 > dp[i] and height_array[j] < height_array[i]:
                dp[i] = dp[j] + 1
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if dp2[j] + 1 > dp2[i] and height_array[j] < height_array[i]:
                dp2[i] = dp2[j] + 1
    return max(dp[i] + dp2[i] for i in range(n)) - 1


dp = [1] * n
dp2 = [1] * n
print(n - dynamic_programming())
