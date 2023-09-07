# LINK: https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # character : frequency
        chDict = {}
        l, r = 0, 0
        maxSub = 0
        for r in range(len(s)):
            ch = s[r]
            # increment letter frequency
            chDict[ch] = 1 + chDict.get(ch, 0)
            # distance from l and r ptr AKA total number of characters
            window = r - l + 1

            # we take the total number of characters - the most frequent letter and see
            # if k is sufficient
            while (window - max(chDict.values())) > k:
                # if insufficient, close the window by one, update the chDict, and recalc the window
                leftMostCh = s[l]
                chDict[leftMostCh] -= 1
                l += 1
                window = r - l + 1
            
            maxSub = max(maxSub, window)

        return maxSub