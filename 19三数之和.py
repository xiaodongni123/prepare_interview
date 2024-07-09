# @Date ：2024/07/08 20:55
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # 首先对数组进行排序
        res = []
        n = len(nums)

        for i in range(n):
            # 避免重复的三元组
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 使用双指针方法寻找另外两个数
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # 避免重复的结果
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res


# 示例用法
nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))  # 输出: [[-1, -1, 2], [-1, 0, 1]]
