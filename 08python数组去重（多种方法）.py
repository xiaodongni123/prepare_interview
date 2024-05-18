# @Date ：2024/05/18 15:44

# 1. 使用集合（set）：
original_list = [1, 2, 3, 4, 3, 2, 1]
# unique_list = list(set(original_list))
unique_list = list(set(original_list))


# 2. 使用列表推导式：
original_list = [1, 2, 3, 4, 3, 2, 1]
unique_list = []
[unique_list.append(x) for x in original_list if x not in unique_list]
# [unique_list.append(x) for x in original_list if x not in unique_list]

# 3. 使用循环遍历：
original_list = [1, 2, 3, 4, 3, 2, 1]
unique_list = []
for x in original_list:
    if x not in unique_list:
        unique_list.append(x)

# 使用 NumPy 库（适用于数组而不是列表）：
import numpy as np
original_array = np.array([1, 2, 3, 4, 3, 2, 1])
unique_array = np.unique(original_array)