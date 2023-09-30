#LINK: https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # range goes from [1, 2, ... n]
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            # when we reach a "bad version", check if the
            # version prior is bad as well. If it is bad, 
            # return the mid ptr, otherwise, move the right
            # ptr back as the bad versions are further left
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                r = mid - 1

            else:
                if isBadVersion(mid + 1):
                    return mid + 1
                l = mid + 1
            
        return -1