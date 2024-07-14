# @Date ：2024/07/14 18:06
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 否则右半部分有序
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# 示例用法
solution = Solution()

# 示例 1
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(solution.search(nums1, target1))  # 输出: 4

# 示例 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
print(solution.search(nums2, target2))  # 输出: -1

# 示例 3
nums3 = [1]
target3 = 0
print(solution.search(nums3, target3))  # 输出: -1
