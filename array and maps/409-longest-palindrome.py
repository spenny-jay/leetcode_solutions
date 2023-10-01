# LINK: https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqs = {}
        # track number of letters that appear an odd # of times
        odd_nums = 0

        for ch in s:
            # update the count for a letter
            freqs[ch] = freqs.get(ch, 0) + 1
            # if the letter has appeared an odd number of times
            if freqs[ch] % 2 == 1:
                odd_nums += 1
            # occurs when we come across the same letter, thus
            # it is no longer odd
            else:
                odd_nums -= 1

        # if we have only come across 1 odd_num, it can be included in
        # the palindrome, otherwise omit all the other odd characters
        # excluding 1
        return len(s) if odd_nums <= 1 else len(s) - odd_nums + 1