def qsort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    standard = arr[0] # 基准值
    less=[] # 比基准值小的
    greater=[] # 比基准值大的
    for i in range(1, len(arr)):
        if arr[i] < standard:
            less.append(arr[i])
        elif arr[i] >= standard:
            greater.append(arr[i])
    arr = qsort(less) + [standard] + qsort(greater) # 递归
    return arr


arr = [3, 5, 2, 6, 8, 1, 0]
print(qsort(arr))
