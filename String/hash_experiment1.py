B = 26  # 假设字符串中只有大写字母，那么B=26，用于构建26进制
mod = 1000000000007  # 取一个大质数，用于取模，防止溢出


def hash(s, mod):  # 哈希函数，计算主串
    h = [0] * (len(s))
    h[0] = ord(s[0]) - ord("A")
    for i in range(1, len(s)):
        h[i] = (h[i - 1] * B + ord(s[i]) - ord("A")) % mod
    return h


p = input()
s = input()

p_hash = 0  # 模式串的哈希值
for c in p:
    p_hash = p_hash * B + ord(c) - ord("A")
    p_hash %= mod  # 一定要记得取模，否则有可能溢出
s_hash = hash(s, mod)
con = B ** len(p) % mod
ans = 0
if p_hash == s_hash[len(p) - 1]:  # 判断第一个子串是否匹配
    ans += 1
for i in range(1, len(s) - len(p) + 1):  # 从第二个子串开始判断匹配
    if (s_hash[i + len(p) - 1] - s_hash[i - 1] * con + mod) % mod == p_hash:
        ans += 1

print(ans)
