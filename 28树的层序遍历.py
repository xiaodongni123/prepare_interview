# @Date ：2024/07/13 19:57
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.pop(0)
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result


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
root1 = build_tree_from_list([3, 9, 20, None, None, 15, 7])
solution = Solution()
print(solution.levelOrder(root1))  # 输出: [[3], [9, 20], [15, 7]]

# 示例 2
root2 = build_tree_from_list([1])
print(solution.levelOrder(root2))  # 输出: [[1]]

# 示例 3
root3 = build_tree_from_list([])
print(solution.levelOrder(root3))  # 输出: []
