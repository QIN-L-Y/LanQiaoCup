# https://www.lanqiao.cn/problems/3423/learning/
n,k=map(int,input().split())
def dp():
    ans=[]
    ans.append(1)
    for i in range(n):
        if i-k-1>=0:
            ans.append(ans[i-k-1]+ans[i-1])
        else:
            ans.append(ans[i-1]+1)
print(dp())
