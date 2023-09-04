# LINK: https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        # stores all nodes for the current level
        queue = deque([ root ])
        # goes level by level (BFS)
        while queue:
            # represents rightmost element on the current level
            curr = None
            # iterate through the current level
            for _ in range(len(queue)):
                curr = queue.popleft()
                # add nodes from the next level
                # since add nodes from left-to-right per level, the rightmost
                # node will be the last one in the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # add the rightmost node on this level to the result
            res.append(curr.val)
            
        return res