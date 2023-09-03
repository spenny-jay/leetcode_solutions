# LINK: https://leetcode.com/problems/delete-node-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root
        # if the root value we are at is larger than the key, traverse left
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # if the root value we are at is less than the key, traverse right
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # When we arrive at the node to delete
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # in the scenario where we are at a root node w/ children
            # get to the lowest value on the right side
            curr = root.right
            while curr.left:
                curr = curr.left
            # set the root node to the new root value
            root.val = curr.val
            # recursively reach the lowest value to delete it
            root.right = self.deleteNode(root.right, root.val)
        return root

       
        