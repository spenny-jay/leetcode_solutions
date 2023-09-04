# LINK: https://leetcode.com/problems/house-robber/description/

# test cases
# [2, 1, 3, 4] --> 6
# [2, 7, 9, 3, 1] --> 12


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Memoize the most optimal route at each location
        dp = [None] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            # either choose the adjacent location and maintain its optimal cost
            # or include the current house cost plus the house 2 indexes away
            dp[i + 1] = max(dp[i], nums[i] + dp[i - 1])

        return dp[-1]