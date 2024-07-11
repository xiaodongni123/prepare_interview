# @Date ：2024/07/10 20:20
import random
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, start, end):
        left, right = start, end
        if left >= right:
            return
        mid = random.randint(left, right)
        nums[left], nums[mid] = nums[mid], nums[left]
        p = nums[left]

        while left < right:
            while left < right and nums[right] >= p:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] < p:
                left += 1
            nums[right] = nums[left]
        nums[left] = p
        while left >= 0 and nums[left] == p:
            left -= 1
        while right < len(nums) and nums[right] == p:
            right += 1
        self.quick_sort(nums, start, left)
        self.quick_sort(nums, right, end)
# class Solution(object):
#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         self.quick_sort(nums, 0, len(nums) - 1)
#         return nums
#
#     def quick_sort(self, nums, start, end):
#         left, right = start, end
#         if left >= right:
#             return
#         mid = random.randint(left, right)
#         nums[left], nums[mid] = nums[mid], nums[left]
#         p = nums[left]
#         while left < right:
#             while left < right and nums[right] >= p:
#                 right -= 1
#             nums[left] = nums[right]
#             while left < right and nums[left] < p:
#                 left += 1
#             nums[right] = nums[left]
#         nums[left] = p
#         while left >= 0 and nums[left] == p:
#             left -= 1
#         while right < len(nums) and nums[right] == p:
#             right += 1
#         self.quick_sort(nums, start, left)
#         self.quick_sort(nums, right, end)
solution = Solution()
nums1 = [5, 2, 3, 1]
print(solution.sortArray(nums1))  # 输出: [1, 2, 3, 5]
