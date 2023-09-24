# LINK: https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            elif len(stack) > 0 and (
                bracket == ")" and stack[-1] == "(" or 
                bracket == "}" and stack[-1] == "{" or 
                bracket == "]" and stack[-1] == "["
            ):
                stack.pop()
            else:
                return False

        return len(stack) == 0
        