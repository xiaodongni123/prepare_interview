# @Date ：2024/07/12 21:02
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 示例用法
def build_tree_from_list(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# 示例 1
p1 = build_tree_from_list([1, 2, 3])
q1 = build_tree_from_list([1, 2, 3])
solution = Solution()
print(solution.isSameTree(p1, q1))  # 输出: True

# 示例 2
p2 = build_tree_from_list([1, 2])
q2 = build_tree_from_list([1, None, 2])
print(solution.isSameTree(p2, q2))  # 输出: False

# 示例 3
p3 = build_tree_from_list([1, 2, 1])
q3 = build_tree_from_list([1, 1, 2])
print(solution.isSameTree(p3, q3))  # 输出: False
