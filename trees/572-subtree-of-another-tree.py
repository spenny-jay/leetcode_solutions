# LINK: https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # edge case when the subRoot is null
        if not subRoot: return True
        # if the root is null and subRoot isn't, then the subRoot cannot be in the root
        if not root: return False
        # We check if where we are in the root and the subRoot are identical
        if self.isSame(root, subRoot):
            return True
        # Proceed to iterate through each end of the root
        # Note: we use "or" here are we only care if the subtree is on one side
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # helper function to see if the two nodes and their children are equivalent
    # We need this because isSubtree() should not iterate through the subRoot, 
    # rather it should keep seeking for the element that matches the subRoot's initial node
    # in root
    def isSame(self, p, q):
        # if both nodes are null, that means we have sucessfully iterated
        # through both trees
        if not p and not q:
            return True
        # if only one of currently traversed nodes is null, then they do not match
        if not p or not q:
            return False
        # proceed to iterate through both trees on each end and check if the vals are equivalent
        return p.val == q.val and self.isSame(p.right, q.right) and self.isSame(p.left, q.left)
