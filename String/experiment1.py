# https://www.lanqiao.cn/problems/2047/learning/
def cal_next(p):
    j = 0
    k = -1
    next = [0] * len(p)
    next[0] = -1
    while j < len(p) - 1:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            next[j] = k
        else:
            k = next[k]
    return next


def kmp(s, p):
    next = cal_next(p)
    i = 0
    j = 0
    while i < len(s) and j < len(p):
        if s[i] == p[j] or j == -1:
            i += 1
            j += 1
        else:
            j = next[j]
    return (
        i - j if j == len(p) else -1
    )  # i-j是匹配的起始位置，j==len(p)表示匹配成功，返回匹配的起始位置，否则返回-1


# 主要思路：每次找到一个匹配的子串，就将主串和模式串的指针向匹配起始点向后移动1位，继续匹配
p = input()
s = input()
i = 0
ans = 0
len_s = len(s)
while i + len(p) <= len_s:
    if kmp(s, p) != -1:
        ans += 1
        i = kmp(s, p) + 1  # i是下一次匹配的起始位置，所以要加1
        s = s[kmp(s, p) + 1 :]  # s是下一次匹配的主串
    else:
        break
print(ans)
