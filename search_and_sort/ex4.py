# 五子棋
# 定义二维数组
mp = [[0] * 5 for i in range(5)]
ans = 0


def check():
    global ans
    # 检查是否胜利
    for i in range(5):
        if sum(mp[i]) % 5 == 0:
            return
    for j in range(5):
        if sum(mp[i][j] for i in range(5)) % 5 == 0:  # 这里应该是mp[i][j]而不是mp[i]
            return
    # 主对角线
    if sum(mp[i][i] for i in range(5)) % 5 == 0:
        return
    # 副对角线
    if sum(mp[i][4 - i] for i in range(5)) % 5 == 0:
        return
    # 如果没有胜利，答案加一
    ans += 1


def dfs(num, ones):  # 传入白棋的数量
    if ones > 13:
        return
    if num == 25:
        if ones == 13:
            check()
        return

    x = num // 5
    y = num % 5
    mp[x][y] = 1
    dfs(num + 1, ones + 1)
    mp[x][y] = 0
    dfs(num + 1, ones)


dfs(0, 0)
print(ans)
