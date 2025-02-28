# 364 跳石头
def check(mid, a):  # 检查mid是否满足条件或合法性
    cnt = 0  # 计数器，记录移走的石头数量
    # 什么时候需要移走该石头？当下一个石头与当前石头的距离小于mid时，需要移走该石头
    b = a[:]  # 复制一份a，避免修改原数组
    for i in range(1, len(a)):  # 从1开始防止起始石头被移走，终止与len(a) - 1，防止终点石头被移走
        if b[i] - b[i - 1] < mid:
            cnt += 1
            b[i] = b[i - 1]  # 当前石头移动到上一个石头的位置, 相当于移走当前石头
    if cnt > M:
        return False
    return True


L, N, M = map(int, input().split())
a = [0]  # 起始石头
for i in range(N):
    a.append(int(input()))
a.append(L)  # 终点石头
# 二分核心思路：移走的石头越多，则最小跳跃距离肯定越大，这是单调性所体现的地方
# 以最小条约距离作为二分查找的目标，然后检查是否满足条件
left = 1  # 二分查找的左边界
right = L  # 二分查找的右边界
ans = 1 # 最终答案，切忌不是mid，因为mid是不断变化的，而ans是最终的结果
while left <= right:  # 二分查找的终止条件
    mid = (left + right) // 2  # 二分查找的中间值
    if check(mid, a):  # 检查mid是否满足条件，即在mid的情况下是否能保证移除的石头数量不超过M
        ans = mid
        left = mid + 1  # 如果可以不超过M，说明跳的还不够远，mid可以增大，向右边界查找，即left=mid+1
    else:
        right = mid - 1
print(ans)


