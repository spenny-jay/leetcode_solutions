# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # add and pop from the end of the list
        stack = []
        # starting point, represents the current leftmost element
        curr = root
        # we have an "or" here b/c stack is initally empty so we rely on
        # if curr is not None to enter the loop for the first time
        # IN ORDER TRAVERSAL
        while curr or stack:
            # add elements as we traverse to the leftmost element
            while curr:
                stack.append(curr)
                curr = curr.left

            # current leftmost element
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            # This is ok to be None, if the stack has elements, it will skip to
            # line 25 and pop the next element
            curr = curr.right

        return -1