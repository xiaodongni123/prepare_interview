# @Date ：2024/07/11 19:40
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 初始化当前子数组和最大子数组和
        current_sum = max_sum = nums[0]

        # 从第二个元素开始遍历
        for num in nums[1:]:
            # 更新当前子数组和，如果当前子数组和小于当前元素，则抛弃当前子数组，从当前元素重新开始
            current_sum = max(num, current_sum + num)
            # 更新最大子数组和
            max_sum = max(max_sum, current_sum)

        return max_sum


# 示例用法
solution = Solution()
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(solution.maxSubArray(nums1))  # 输出: 6

nums2 = [1]
print(solution.maxSubArray(nums2))  # 输出: 1

nums3 = [5, 4, -1, 7, 8]
print(solution.maxSubArray(nums3))  # 输出: 23
