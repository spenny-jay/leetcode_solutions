# LINK: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a helper function to maintain the "good" value on the path
        def dfs(root, goodVal):
            # reach the end of the path, no more good values
            if not root:
                return 0

            # if we reach node that is "good", increment total by one
            # and update the goodVal to root.val for the subsequent calls
            if root.val >= goodVal:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)

            # if a "good" value was not found, traverse the tree and
            # maintain the same "good" value
            return dfs(root.left, goodVal) + dfs(root.right, goodVal)
            
        return dfs(root, root.val)