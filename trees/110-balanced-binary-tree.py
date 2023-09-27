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
            # use depth as returned from children subtrees (+ current node)
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            diff = abs(left - right)
            # if the left side is deeper than the right or vice versa
            # invalidate all future paths with -1
            if diff > 2 or left == 0 or right == 0:
                return -1

            # otherwise, increment the depth!
            return 1 + max(left, right)
            

        # -1 indicates that a diff > 2 was encountered in a path
        return dfs(root) != -1
        

