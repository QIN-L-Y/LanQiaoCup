# 3820 混境之地
from functools import (
    lru_cache,
)  # 使用lru_cache装饰器，可以缓存函数的返回值，相当于记忆化搜索，避免重复计算

n, m, k = map(int, input().split())
A, B, C, D = map(int, input().split())
A, B, C, D = A - 1, B - 1, C - 1, D - 1  # 题目的下标是从1开始，为了方便计算，将坐标减一
Map = []
for i in range(n):
    Map.append(list(map(int, input().split())))


#  DFS函数传入参数说明：x,y分别代表当前坐标，z表示是否使用喷气背包
#  核心思路：二种情况返回True：1.当前坐标就是出口 2.向下一个位置搜索递归成功找到出口
@lru_cache(None)
def DFS(x, y, z):
    # 递归出口：当前坐标为出口了
    if x == C and y == D:
        return True
    # 如果不在出口，向四周搜索可走的位置
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(4):
        delta_x, delta_y = dir[i]
        xx, yy = x + delta_x, y + delta_y
        # 判断是否越界
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if Map[xx][yy] < Map[x][y]:  # 如果下一个位置比当前位置低,向下一个位置搜索
            if DFS(xx, yy, z):  # 如果下一个位置搜索成功，返回True
                return True
        if (
            z == False and Map[xx][yy] <= Map[x][y] + k
        ):  # 如果当前位置没有使用喷气背包，且下一个位置比当前位置高的小于等于k
            if DFS(xx, yy, True):
                return True
    return False  # 如果四个方向都搜索失败，返回False


print(
    "No" if DFS(A, B, False) == False else "Yes"
)  # 从起点开始搜索，初始没有使用喷气背包
# 如果不使用lrc_cache装饰器，自己写记忆化搜索
dic = {}  # 用字典保存当前位置是否可以搜索成功


def DFS_mem(x, y, z):
    # 递归出口：当前坐标为出口了
    if x == C and y == D:
        return True
    # 如果不在出口，向四周搜索可走的位置
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(4):
        delta_x, delta_y = dir[i]
        xx, yy = x + delta_x, y + delta_y
        # 判断是否越界
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        if (xx, yy, z) in dic:
            return dic[(xx, yy, z)]
        else:
            if Map[xx][yy] < Map[x][y]:  # 如果下一个位置比当前位置低,向下一个位置搜索
                if DFS(xx, yy, z):  # 如果下一个位置搜索成功，返回True
                    dic[(xx, yy, z)] = True
                    return True
            if (
                z == False and Map[xx][yy] <= Map[x][y] + k
            ):  # 如果当前位置没有使用喷气背包，且下一个位置比当前位置高的小于等于k
                if DFS(xx, yy, True):
                    dic[(xx, yy, z)] = True
                    return True
    dic[(x, y, z)] = False
    return False  # 如果四个方向都搜索失败，返回False


print(
    "No" if DFS_mem(A, B, False) == False else "Yes"
)  # 从起点开始搜索，初始没有使用喷气背包
