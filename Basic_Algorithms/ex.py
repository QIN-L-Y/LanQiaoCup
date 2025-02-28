# 3419小蓝的平衡字符串
# https://www.lanqiao.cn/problems/3419/learning/
str = input()
ans = 0
gaps = 0  # gaps是L和Q数量的差值，属于前缀和的思想
dict = {}  # 保存gaps的值第一次对应的下标
# 总思路：什么叫平衡串？就是两个遍历位置的gaps相等时，说明中间的L和Q数量相等
# 遍历字符串，如果gaps的值第一次出现，就保存下标，如果gaps的值再次出现，就计算两次出现的下标之差，更新ans
for i in range(0, len(str)):
    if str[i] == 'L':
        gaps += 1
    elif str[i] == 'Q':
        gaps -= 1
    if gaps not in dict:
        dict[gaps] = i
    elif gaps in dict:
        if ans < i - dict[gaps]:
            ans = i - dict[gaps]
print(ans)
