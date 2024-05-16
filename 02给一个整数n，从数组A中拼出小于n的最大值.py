# -*- coding:utf-8 -*-
n = 1234
A = [1, 3, 5, 2, 6, 9, 8, 7]

def max_less_than_n(n, A):
    A.sort(reverse=True)  # 将数组A按逆序排列
    result = []
    total = 0
    for dig in A:

        total *= 10
        total += dig
        if total < n:
            result.append(dig)
        else:
            total //= 10

    return result

print(max_less_than_n(n, A))

"""
算法思想：
1. 首先将数组倒序
2. 从数组里面取出单个数，组建整体数字，与目标数字对比
3. 数字大与目标数字，退回；数字小于目标数字，添加到新数组
"""


