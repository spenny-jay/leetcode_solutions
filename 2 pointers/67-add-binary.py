# LINK: https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        # start at the first digit of each string
        i, j = len(a) - 1, len(b) - 1
        # tracks whether the current digits will
        # carry a one to the next sum
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            
            if j >= 0:
                carry += int(b[j])
                j -= 1
            # (1 + 1) % 2 = 0
            # (0 + 0) % 2 = 0
            # (0 + 1) % 2 = 1
            res = str(carry % 2) + res
            # for the next sum, carry will be
            # either set to be 0 or 1 depending
            # if its divisible by 2 (1 + 1 was encountered)
            carry = carry // 2
        # if there is a remaining carry (1) 
        if carry % 2 == 1:
            res = str(1) + res

        return res
