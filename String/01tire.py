# https://www.lanqiao.cn/problems/8616/learning/
class Tree:
    def __init__(self):
        self.children = {}
        self.isleaf = False

    def insert(self, arr):
        node = self
        for i in range(32):
            key = arr << (31 - i) & 1
            if key not in node.children.keys():
                node.children[key]
            node = node.children[key]
        node.isleaf = True
