s = input()
s = "#" + "#".join(s) + "#"  # 插入#，方便处理奇偶


def cal_dp(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return (
        right - 1 - (left + 1) + 1
    ) // 2  # 返回dp数组的值,为什么right-1，left+1，因为while循环结束时，left和right已经不满足条件了，所以真正的长度是上一轮


dp = [0] * len(s)
right = 0
center = 0
for i in range(1, len(s)):
    if i > right:  # i在right的右边，没有任何信息可以利用，只能暴力
        dp[i] = cal_dp(s, i, i)
        center = i
        right = i + dp[i]
    elif i + dp[2 * center - i] < right:  # i在right的左边，使用对称性
        dp[i] = dp[2 * center - i]
    else:  # i在right的右边，right和i之间的信息不能利用，使用暴力，但是可以确定初始右端点是right
        dp[i] = cal_dp(s, 2 * i - right, right)
        center = i
        right = i + dp[i]
print(dp)
print(
    max(dp)
)  # 输出最长回文子串的长度，为什么不用乘以2，因为dp数组的值是以#为中心的长度，而原字符串的长度是以中心的长度
