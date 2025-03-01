# https://www.lanqiao.cn/problems/1189/learning/
def LCS():
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if (
                a[i] == b[j]
            ):  # 如果a数组的第i个数和b数组的第j个数相等，那么最长公共子序列长度就等于a数组的第i-1个数和b数组的第j-1个数的最长公共子序列长度加1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


N, M = map(int, input().split())
a = [0] + list(
    map(int, input().split())
)  # 注意要加0，因为要考虑空字符串的情况，这里两个字符串都加0并不会影响结果，因为LCS函数中循环从1开始的
b = [0] + list(map(int, input().split()))
dp = [
    [0] * (1 + M) for i in range(N + 1)
]  # dp[i][j]表示a数组前i个数和b数组前j个数的最长公共子序列，为什么要比原数组长度多1，这样方便计算
LCS()
print(dp[N][M])
