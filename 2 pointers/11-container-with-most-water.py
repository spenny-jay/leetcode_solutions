class Solution:
    def maxArea(self, height: List[int]) -> int:
        # start at each end of the height list and slowly close the pointers
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            width = r - l
            # take the minimum bc that is the current limit of water that can be stored
            currArea = width * min(height[l], height[r])
            res = max(res, currArea)
            # increment the pointer of the lowest height
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return res
            

            