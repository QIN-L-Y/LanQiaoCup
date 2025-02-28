# https://www.lanqiao.cn/problems/3751/learning/
class Tree:
    def __init__(self):
        self.children = (
            {}
        )  # 表示子节点，即当前节点向下走的后续节点，用字典表示，key是子节点的值，value是子节点的Tree对象
        self.isleaf = False  # 表示是否是叶节点，即是否是一个单词的结束节点的标志
        self.number = 0  # 表示有多少个单词经过这个节点

    def insert(self, word):  # 插入一个单词
        node = self  # 从根节点开始，为什么self是根节点，因为在调用insert函数时，是通过根节点调用的
        for char in word:
            node.number += 1
            if char in node.children.keys():  # 如果子节点中有这个字符，就继续往下走
                node = node.children[
                    char
                ]  # node.children[char]表示字典key为char的value，即子节点的Tree对象
            else:  # 如果子节点中没有这个字符，就新建一个子节点
                node.children[char] = (
                    Tree()
                )  # 表示给字典key为char的value，赋予一个新的Tree对象
                node = node.children[char]

        node.isleaf = True  # 当单词插入完毕，将isleaf设置为True
        node.number += 1  # 最后一个节点的number加1，为什么要单独加，因为最后一个节点不会在for循环中加

    def prefix(self, word):
        node = self
        num = 0
        for char in word:
            node = node.children[char]  # 如果子节点中有这个字符，就继续往下走
            if (
                node.number == 1
            ):  # 如果这个节点只有一个单词经过，那就说明上一个节点是这个公共前缀的最后一个节点
                return num
            num += 1
        return num


# 字典树根节点
root = Tree()
N = int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)
    root.insert(s)
for s in S:
    print(root.prefix(s))
