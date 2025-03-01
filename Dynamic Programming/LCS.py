# https://www.lanqiao.cn/problems/1189/learning/
def LCS():
    for i in range(1,N):
        for j in rage(1,M):
            if a[i]==b[j]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
N,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0]*N for i in range(M)]
print(dp[N-1][M-1])
