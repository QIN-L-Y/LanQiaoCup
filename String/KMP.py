# KMP 算法
# 整体思路：当出现字符串不匹配时，不需要回溯 i 指针，而是利用已经得到的部分匹配结果将模式串向右移动，从而减少不必要的比较
# 模式串和主串：模式串是要匹配的字符串，主串是被匹配的字符串
# 1. 计算 next 数组，next 数组的含义是：当模式串中的字符与主串中的字符不匹配时，模式串应该移动到的位置，即模式串的前缀与后缀的最长公共前缀的长度
# 比如在匹配中，模式串的第5个字符没对上，next[5] = 2，表示模式串前缀长度为5时，有长度为2的相同前后缀，模式串应该移动到第3个字符进行匹配
# 2. 利用 next 数组进行匹配，当出现不匹配时，模式串移动到 next[j] 的位置，继续匹配


# calculate_next 函数：计算 next 数组，k 表示前缀，j 表示当前位置，j-k表示后缀
def calculate_next(p):
    next = [0] * len(p)
    next[0] = -1  # 第一个字符的next值为-1
    j = 0
    k = -1
    while j < len(p) - 1:
        if (
            k == -1 or p[j] == p[k]
        ):  # k == -1 表示前缀不存在，p[j] == p[k] 表示前缀和后缀相等
            j += 1
            k += 1
            next[j] = k
        else:  # 不相等，k 移动到 next[k] 的位置
            k = next[k]
    return next


def kmp(s, p):
    next = calculate_next(p)
    print(next)
    i = 0
    j = 0
    while i < len(s) and j < len(p):
        if (
            s[i] == p[j] or j == -1
        ):  # j == -1 表示前缀不存在，这个一定要有，否则会出现死循环，比如第一个字符就不匹配，那么 j = next[j] = -1，i += 1，j = 0，再次不匹配，j = -1，i += 1，j = 0，如此循环
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(p):
        return True
    else:
        return False


s = "ababcbbcacbab"
p = "bbcaba"
print(kmp(s, p))
