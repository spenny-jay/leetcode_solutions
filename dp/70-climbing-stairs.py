# LINK: https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        # values 1 - 3 will be n
        if n <= 3: return n
        # used to memoize results
        dp = [0] * n
        # initialize dp (dp[0] represents 1 stair, dp[1] represents 2 stairs, ... 
        # dp[n] represents n stairs)
        dp[0] = 1
        dp[1] = 2
        # Every step count is a combination between the prior two
        # (ex: combines results when the user move either 1 or 2 steps)
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        # return number of combinations when there are n steps
        return dp[-1]