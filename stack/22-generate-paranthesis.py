# LINK: https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # start: number of open paranthesis
        # closed: number of colosed paranthesis
        def helper(currStr, start, end):
            # when we reach the total # of paranthesis 
            if start + end == n * 2:
                res.append(currStr)
                return
            
            # If we are still under the allowed # of open paranthesis
            if start < n:
               helper(currStr + "(", start + 1, end)

            # If we are able to add an end paranthesis, cannot have one without an open paranthesis
            if end < start:
                helper(currStr + ")", start, end + 1)


        helper("", 0, 0)
        return res