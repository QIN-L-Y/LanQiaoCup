# 3382区间次方和
# https://www.lanqiao.cn/problems/3382/learning/
# 为了更快的计算区间次方和，可以先计算出所有次方和存储起来，再直接查表
def prefixes(a):  #求前缀和
    sum = [0] * (len(a))
    sum[0] = a[0]
    for i in range(len(a)):
        sum[i] = sum[i - 1] + a[i]
    return sum


n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a  #下标从1开始
sum = []  #存储a的各次前缀和
for i in range(1, 6):
    sum.append(prefixes(list(x ** i for x in a)))  #计算a的i次前缀和
ans = 0
for i in range(m):
    l, r, k = map(int, input().split())
    ans = sum[k - 1][r] - sum[k - 1][l - 1]
    print(ans%1000000007)
