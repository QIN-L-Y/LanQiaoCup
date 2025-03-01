# https://www.lanqiao.cn/problems/742/learning/
n = int(input())
height_array = list((map(int, input().split())))


def dynamic_programming():
    for i in range(1, n):
        dp[i] = 1
        dp2[i]=1
        for j in range(i):
            if dp[j] + 1 > dp[i] and height_array[j] < height_array[i]:
                dp[i] = dp[j] + 1
        for j in range(i+1,n):
            if dp2[j]+1>dp[i] and height_array[j]<height_array[i]:
                dp2[i]=dp2[j+1]
    return max(dp)+max(dp2)


dp = [0] * n
dp2= [0] * n
dp[0] = 1

print(n-dynamic_programming())

