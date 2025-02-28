# DFS经典回溯模板：全排列
n = int(input())
path = [0 for i in range(n)]  # 路径数组，存储当前的路径
vis = [0 for j in range(n)]  # 标记数组，标记元素是否被访问


def DFS(depth):
    if depth == n:
        print(path)
        return
    # 对当前节点下的所有可能的选择进行搜索
    for i in range(n):
        if vis[i] == False:  # 如果当前元素没有被访问,那么就选择这个元素
            vis[i] = True  # 标记当前元素已经被访问
            path[depth] = i + 1  # 将当前元素加入路径
            DFS(depth + 1)
            # 回溯，需要标记当前元素为未访问
            vis[i] = False


DFS(0)  # 从第0层开始搜索
