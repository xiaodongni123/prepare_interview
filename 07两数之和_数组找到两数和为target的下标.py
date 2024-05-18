# @Date ：2024/05/18 13:34

"""
双指针做法，时间复杂度nlogn：
1. 先排序
2. 双指针，一个在前面，一个后面，相加，与目标值对比
"""
# def two_sum(nums, target):
#     nums.sort()
#
#     left, right = 0, len(nums)-1
#     while(left < right):
#         p = nums[left] + nums[right]
#         if p == target:
#             return [left, right]
#         elif p < target:
#             left += 1
#         else:
#             right -= 1
#     return None


"""
hash表的做法,时间复杂度为n
"""
def two_sum(nums, target):
    # 首先创建一个hashmap
    num_map = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i
    return None

if __name__ == '__main__':
    # 示例输入
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
