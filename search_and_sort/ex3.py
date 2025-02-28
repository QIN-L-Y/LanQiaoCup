# 216 地宫取宝
n, m, k = map(int, input().split())
Value = []
for i in range(n):
    Value.append(list(map(int, input().split())))
dic = {}


# DFS传入参数：当前坐标x，y、当前拿到的总数，当前拿到宝物的最大值，有了这四个参数，就可以唯一确定一个解
def DFS(x, y, cur_sum, cur_max):
    # 递归出口：如果出口位置刚好拿到k个，或者还差一个并且最后一个宝物的价值大于当前最大值，那么就是一种方案
    if x == n - 1 and y == m - 1:
        if cur_sum == k or (cur_sum == k - 1 and Value[n - 1][m - 1] > cur_max):
            return 1
        else:
            return 0
    if (x, y, cur_sum, cur_max) in dic.keys():  # 如果已经计算过了，那么直接返回
        return dic[(x, y, cur_sum, cur_max)]
    dir = [(0, 1), (1, 0)]  # 只能向右或者向下走
    ans = 0  # 这个ans不能使用全局变量，否则ans会一直累加
    for i in range(2):
        delta_x, delta_y = dir[i]
        xx, yy = x + delta_x, y + delta_y
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        else:
            if Value[x][y] > cur_max:
                ans += DFS(xx, yy, cur_sum + 1, Value[x][y])  # 拿了当前宝贝后向右或下走
            ans += DFS(
                xx, yy, cur_sum, cur_max
            )  # 注意，当前宝贝价值大于最大值时也可以选择不拿
    dic[(x, y, cur_sum, cur_max)] = ans
    return ans % (1e9 + 7)


print(
    int(DFS(0, 0, 0, -1))
)  # 从(0,0)开始，拿到的宝物价值为0，最大价值为-1（注意题目中某地价值可能为0）
