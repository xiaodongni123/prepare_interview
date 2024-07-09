# @Date ：2024/07/09 19:26
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         # 初始化两个指针，一个指向数组的起始位置，一个指向数组的末尾位置
#         left = 0
#         right = len(height) - 1
#         max_area = 0
#
#         # 当左指针小于右指针时，进行迭代
#         while left < right:
#             # 计算当前区域的宽度
#             width = right - left
#             # 计算当前区域的高度（取较小的那个）
#             current_height = min(height[left], height[right])
#             # 计算当前区域的面积
#             current_area = width * current_height
#             # 更新最大面积
#             max_area = max(max_area, current_area)
#
#             # 移动较小的那条线
#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#
#         # 返回最大面积
#         return max_area

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = current_height * width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# 示例用法
solution = Solution()
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solution.maxArea(height1))  # 输出: 49

height2 = [1, 1]
print(solution.maxArea(height2))  # 输出: 1
