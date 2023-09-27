# LINK: https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Maintain across subtrees (note: counts # of edges, not nodes)
        self.res = 0
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            # checks if the current # of edges between the two subtrees
            # are the greatest # encountered so far
            self.res = max(left + right, self.res)

            # return the greater of the two subtrees and add another edge
            return max(left, right) + 1
            
        dfs(root)
        return self.res
        
