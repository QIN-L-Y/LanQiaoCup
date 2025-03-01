# https://www.lanqiao.cn/problems/8616/learning/
class Tree:  # 注意不需要加括号
    def __init__(self):
        self.children = [None, None]
        self.isleaf = 0

    def insert(self, number):  # 用于构建01trie树
        node = self
        for i in range(32):
            key = (number >> (31 - i)) & 1  # 从32位开始存入，防止各数的二进制长度不一致
            if node.children[key] is None:  # 如果子节点不存在，就新建一个子节点
                node.children[key] = Tree()  # 初始化子节点
            node = node.children[key]
        node.isleaf = number

    def search(self, number):  # 用于搜索最大异或和
        node = self
        for i in range(32):
            binary = (number >> (31 - i)) & 1
            if (
                node.children[binary ^ 1] is not None
            ):  # 如果存在相反的子节点，就往相反的子节点走
                node = node.children[binary ^ 1]
            else:  # 否则就往原来的子节点走
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
