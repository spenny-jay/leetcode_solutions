# LINK: https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            diff = abs(left - right)
            if diff > 2 or left == 0 or right == 0:
                return -1

            return 1 + max(left, right)
            


        return dfs(root) != -1
        

