# https://www.lanqiao.cn/problems/3423/learning/
n, k = map(int, input().split())
mod = 1e9 + 7


def dp():
    ans = []
    ans.append(2)
    for i in range(1, n):
        if i - k - 1 >= 0:
            ans.append((ans[i - k - 1] + ans[i - 1]) % mod)
        else:
            ans.append((ans[i - 1] + 1) % mod)

    return ans[-1]


print(int(dp()))
