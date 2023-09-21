# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast, slow = head, head
        # goal: get fast to be at the nth position
        # ex) n = 8, len(head) == 10
        # that means remove the 2nd node, but we want fast to be 
        # at the 8th node to help figure out how many nodes away we are
        # from the end of the list
        for _ in range(n):
            fast = fast.next 
            
        # if n turns out to be the whole length of the list,
        # remove the 1st node in the list
        if not fast:
            return slow.next

        # goal: Now that we have a gap of n node, once fast reaches the end, 
        # slow will be n nodes away from the end (AKA fast)
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head