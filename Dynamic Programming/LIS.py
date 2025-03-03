# https://www.lanqiao.cn/problems/742/learning/
n = int(input())
height_array = list((map(int, input().split())))


def dynamic_programming():
    for i in range(1, n):  # 寻找以i结尾的最长上升子序列
        for j in range(i):
            if dp[j] + 1 > dp[i] and height_array[j] < height_array[i]:
                dp[i] = dp[j] + 1
    for i in range(n - 1, -1, -1):  # 寻找以i开头的最长上升子序列
        for j in range(n - 1, i, -1):
            if dp2[j] + 1 > dp2[i] and height_array[j] < height_array[i]:
                dp2[i] = dp2[j] + 1
    return (
        max(dp[i] + dp2[i] for i in range(n)) - 1
    )  # 为什么要减1，因为i这个点在长度中被计算了两次


dp = [1] * n  # 记录从左往右的最长上升子序列
dp2 = [1] * n  # 记录从右往左的最长上升子序列
print(n - dynamic_programming())
# ceshi