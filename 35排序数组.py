# @Date ：2024/12/15 20:04
from typing import List  # 导入 List 类型提示


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 辅助函数：合并两个已排序的子数组
        def merge(left: List[int], right: List[int]) -> List[int]:
            merged = []
            while left and right:
                if left[0] < right[0]:
                    merged.append(left.pop(0))
                else:
                    merged.append(right.pop(0))
            # 把剩余部分添加到合并结果中
            merged.extend(left)
            merged.extend(right)
            return merged

        # 递归分治函数
        def merge_sort(nums: List[int]) -> List[int]:
            if len(nums) <= 1:
                return nums
            # 分成两半
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            # 合并排序后的子数组
            return merge(left, right)

        # 调用归并排序并返回结果
        return merge_sort(nums)


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    nums = [38, 27, 43, 3, 9, 82, 10]
    sorted_array = solution.sortArray(nums)
    print("Sorted array:", sorted_array)
