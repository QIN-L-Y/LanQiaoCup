# https://www.lanqiao.cn/problems/8616/learning/
class Tree:
    def __init__(self):
        self.children = {}
        self.isleaf = 0

    def insert(self, number):  # 用于构建01tire树
        node = self
        for i in range(32):
            key = (number >> (31 - i)) & 1  # 从32位开始存入，防止各数的二进制长度不一致
            if key not in node.children:
                node.children[key] = Tree()  # 初始化子节点
            node = node.children[key]
        node.isleaf = number

    def search(self, number):  # 用于搜索最大异或和
        node = self
        for i in range(32):
            binary = (number >> (31 - i)) & 1
            if binary ^ 1 in node.children:
                node = node.children[binary ^ 1]
            else:
                node = node.children[binary]
        return node.isleaf


n = int(input())
arr = list(map(int, input().split()))
root = Tree()
for num in arr:
    root.insert(num)
q = int(input())
ans = []
for i in range(q):
    x = int(input())
    ans.append(root.search(x) ^ x)
for i in range(q):
    print(ans[i])
    print()  
