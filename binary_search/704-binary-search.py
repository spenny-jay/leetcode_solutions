# LINK: https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            # get the average index between the l and r ptrs
            mid = (l + r) // 2
            # if the mid value is too large, eliminate the larger half of the list
            if nums[mid] > target:
                r = mid - 1
            # if the mid value is too small, eliminate the smaller half of the list
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1    