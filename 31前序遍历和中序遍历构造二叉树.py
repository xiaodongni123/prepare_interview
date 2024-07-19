# @Date ：2024/07/18 20:51
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        # 先序遍历的第一个元素是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 在中序遍历中找到根节点的位置
        root_index_in_inorder = inorder.index(root_val)

        # 划分左子树和右子树的元素
        left_inorder = inorder[:root_index_in_inorder]
        right_inorder = inorder[root_index_in_inorder + 1:]

        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        # 递归构建左子树和右子树
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

# 辅助函数用于打印二叉树
def print_tree(root):
    if root:
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)

# 示例用法
solution = Solution()

# 示例 1
preorder1 = [3, 9, 20, 15, 7]
inorder1 = [9, 3, 15, 20, 7]
root1 = solution.buildTree(preorder1, inorder1)
print_tree(root1)  # 输出: 3 9 20 15 7

# 示例 2
preorder2 = [-1]
inorder2 = [-1]
root2 = solution.buildTree(preorder2, inorder2)
print_tree(root2)  # 输出: -1
