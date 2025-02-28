# 二维前缀和与子矩阵和
# 二维前缀和：sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + a[i][j]
# 子矩阵和：sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1]
def getsum(x1, y1, x2, y2):  # 子矩阵和
    return sum[x2][y2] - sum[x2][y1 - 1] - sum[x1 - 1][y2] + sum[x1 - 1][y1 - 1]


def printsum(a):  # 打印二维数组
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(a[i][j], end=' ')
        print()  # 换行


# 输入二维数组
n = int(input())  # n行n列
a = [[0] * (n + 1) for i in range(n + 1)]  # 第一行第一列设置为0，方便使用减法索引，防止溢出
sum = [[0] * (n + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    a[i] = [0] + list(map(int, input().split()))
for i in range(1, n + 1):  # 二维前缀和
    for j in range(1, n + 1):
        sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + a[i][j]
printsum(sum)
