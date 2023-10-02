# LINK: https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # since the slow ptr moves at a rate of n
        # and the fast ptr moves at a rate of 2n
        # when the fast ptr reaches the end, the
        # slow node will be only midway through the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow