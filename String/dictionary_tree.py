class Tree:
    def __init__(self):
        self.children = (
            {}
        )  # 表示子节点，即当前节点向下走的后续节点，用字典表示，key是子节点的值，value是子节点的Tree对象
        self.isleaf = False  # 表示是否是叶节点，即是否是一个单词的结束节点的标志

    def insert(self, word):  # 插入一个单词
        node = self  # 从根节点开始，为什么self是根节点，因为在调用insert函数时，是通过根节点调用的
        for char in word:
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

    def prefix(self, word):  # 判断一个前缀是否存在
        node = self
        for char in word:
            if char not in node.children.keys():
                return False
            node = node.children[char]  # 如果子节点中有这个字符，就继续往下走
        return True


# 字典树根节点
root = Tree()
N, M = list(map(int, input().split()))
for i in range(N):
    root.insert(input())
for i in range(M):
    if root.prefix(input()):
        print("Y")
    else:
        print("N")
