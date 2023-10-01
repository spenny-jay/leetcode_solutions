# LINK: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        # maintains the lowest price when iterating through prices
        minVal = float("inf")
        for price in prices:
            # if a smaller price is encountered, update minVal
            minVal = min(price, minVal)
            # calculate selling the transaction
            returnVal = price - minVal
            # update res if a more profitable returnVal is encountered
            res = max(returnVal, res)
        
        return res


            