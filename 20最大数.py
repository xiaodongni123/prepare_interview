# @Date ：2024/07/08 21:14
from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        # 自定义排序规则
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # 将所有数字转换为字符串
        nums = list(map(str, nums))

        # 按照自定义规则排序
        nums.sort(key=cmp_to_key(compare))

        # 拼接排序后的字符串
        largest_num = ''.join(nums)

        # 特殊情况：如果结果是多个零，返回一个零
        if largest_num[0] == '0':
            return '0'
        else:
            return largest_num


# 示例用法
nums1 = [10, 2]
solution1 = Solution()
print(solution1.largestNumber(nums1))  # 输出: "210"

nums2 = [3, 30, 34, 5, 9]
solution2 = Solution()
print(solution2.largestNumber(nums2))  # 输出: "9534330"
