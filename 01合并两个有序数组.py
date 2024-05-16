# -*- coding:utf-8 -*-
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
def merge_arr(arr1, arr2):
    i, j = 0, 0
    merge = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i += 1
        else:
            merge.append((arr2[j]))
            j += 1

    while i < len(arr1):
        merge.append(arr1[i])
        i += 1

    while j < len(arr2):
        merge.append(arr2[j])
        j += 1
    return merge

print(merge_arr(arr1, arr2))

"""
算法总结：
1. 确定i, j 双指针指向两个数组
2. 三个while循环，第一个对比两个数组，第二个和第三个都是针对其中一个数组，但是一定要移动指针
"""





