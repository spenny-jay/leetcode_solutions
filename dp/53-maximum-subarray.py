#LINK: https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        sums = [0] * len(nums)
        sums[0] = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            # either proceed with the current subarray (sums[i - 1] + nums[i])
            # or start a new subarray (nums[i])
            sums[i] = max(sums[i - 1] + nums[i], nums[i])

            # track the maximum calculated sum
            res = max(res, sums[i])
        return res