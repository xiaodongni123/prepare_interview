# @Date ：2024/07/06 14:33
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 设置两个指针分别指向 nums1 和 nums2 的末尾
        p1 = m - 1
        p2 = n - 1
        # 设置合并后数组的指针，指向合并后的 nums1 末尾
        p = m + n - 1

        # 当 nums2 未处理完时
        while p2 >= 0:
            # 如果 nums1 未处理完并且 nums1[p1] > nums2[p2]，则将 nums1[p1] 放在 nums1[p] 位置
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                # 否则将 nums2[p2] 放在 nums1[p] 位置
                nums1[p] = nums2[p2]
                p2 -= 1
            # 移动合并后数组的指针
            p -= 1

s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)