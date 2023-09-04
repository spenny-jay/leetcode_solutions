# LINK: https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # we start at the 2nd index bc the user can start climbing 
        # at either the 0th or 1st index
        for i in range(2, len(cost)):
            # We look back and add the cheapest of the 2 prior steps
            # since the user can climb 1 or 2 steps at a time
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[-2], cost[-1])