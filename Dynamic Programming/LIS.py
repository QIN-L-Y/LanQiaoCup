# https://www.lanqiao.cn/problems/742/learning/
n = int(input())
height_array = list((map(int, input().split())))


def dynamic_programming():
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if dp[j] + 1 > dp[i] and height_array[j] < height_array[i]:
                dp[i] = dp[j] + 1
        for j in range(i+1,n):
            


dp = [0] * n
dp2= [0] * n
dp[0] = 1

dynamic_programming()
print(max(dp))
print(dp)
