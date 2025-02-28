n = 7  # 七个小朋友，那么dfs的深度也是7
m = 16  # 第一种糖果的个数
l = 9  # 第二种糖果的个数
ans = 0  # 用来存储答案


def DFS(depth, m_left, l_left):
    # 首先明确这是个递归函数，所以需要有一个递归出口
    if depth == n:
        if m_left == 0 and l_left == 0:
            global ans
            ans += 1
        return
    for i in range(min(m_left + 1,6)): # 为什么是min(m_left + 1,6)？因为每个小朋友最多拿5个糖果
        for j in range(min(l_left + 1,6)):
            if 2 <= (i + j) <= 5:  # 如果两种糖果的数量之和在2到5之间，那么就继续搜索
                DFS(depth + 1, m_left - i, l_left - j)


DFS(0, m, l)  # 为什么是从0开始搜索？因为path[0]是第一个小朋友的糖果分配情况
print(ans)
