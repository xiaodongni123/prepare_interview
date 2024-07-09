# @Date ：2024/07/07 12:06
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 基本情况：如果数组长度小于等于1，直接返回数组
        if len(nums) <= 1:
            return nums

        # 分解：将数组分为左右两部分
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])  # 递归排序左半部分
        right = self.sortArray(nums[mid:])  # 递归排序右半部分

        # 合并：将两个有序数组合并成一个有序数组
        return self.merge(left, right)

    def merge(self, left, right):
        sorted_list = []
        i = j = 0

        # 合并两个有序数组
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        # 如果左数组还有剩余，追加到结果数组后面
        sorted_list.extend(left[i:])
        # 如果右数组还有剩余，追加到结果数组后面
        sorted_list.extend(right[j:])

        return sorted_list
nums = [5, 2, 3, 1]
solution = Solution()
sorted_nums = solution.sortArray(nums)
print(sorted_nums)