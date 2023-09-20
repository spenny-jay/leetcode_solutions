# LINK: https://leetcode.com/problems/find-the-duplicate-number/description/

# Similar to Challenge 142
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # Iterate through list till the pointers meet.
        # Fast pointer goes twice as fast as the slow pointer
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # move slow to the start of the list.
        # given the nature of cycles, if there are n nodes before 
        # the start of the cycle, the intersection between slow and fast
        # will occur n nodes away from the end. Thus, we will increment slow
        # and fast n nodes to reach the start of the cycle
        slow = 0
        while True:
            if slow == fast:
                return slow
            fast = nums[fast]
            slow = nums[slow]
            
        
        return -1