# LINK: https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        # fast ptr moves 2x the speed of the slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # once the ptrs meet, that indicates there is a cycle
            if fast == slow:
                # pretty much, when we meet the slow ptr in the cycle,
                # that means the fast ptr has gone through the cycle twice.
                # so, if the entire head is a cycle, the ptrs will meet at the head
                # otherwise, if there are n nodes before the cycle, the two pointers will
                # meet n nodes from the start of the cycle. Thus, we move the slow ptr to 
                # the start and increment the slow and the fast such that they will
                # meet at the beginning of the cycle.
                slow = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
            

        return None