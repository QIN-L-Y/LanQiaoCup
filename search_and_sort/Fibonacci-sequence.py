# 记忆化搜索经典模板：斐波那契数列
# 直接递归改进解法，调用lrc_cache装饰器
from functools import lru_cache
@lru_cache(None)  # 使用lru_cache装饰器，可以缓存函数的返回值，避免重复计算
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


# 记忆化搜索解法
dic = {0: 0, 1: 1}  # 用字典来存储已经计算过的值，在递归的过程中，如果发现已经计算过了，那么就直接取就行


def fib_mem(n):
    if n in dic.keys():
        return dic[n]
    dic[n] = fib_mem(n - 1) + fib_mem(n - 2)
    return dic[n]


# 对比递归解法和记忆化搜索解法的时间
import time

start = time.time()
print(fib(30))
end = time.time()
print("递归解法时间：", end - start)
start = time.time()
print(fib_mem(30))
end = time.time()
print("记忆化搜索解法时间：", end - start)
