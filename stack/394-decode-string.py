# LINK: https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            # keep adding characters till we reach the end of a pattern
            if char is not "]":
                stack.append(char)
            else:
                # grab the pattern's substring (we iterate here as we may
                # concatenate the results of prior pattern)
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop()

                # digits are added to the stack separately, concatenate all digits for the pattern
                # ex) ['1', '0', '0'] --> 100
                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                
                # compute the pattern and add to the top of the stack for potentially
                # the next pattern if its nested
                # ex) ['2', 'a' 'a', 'cccc'] --> 2[a4[c]]
                stack.append(int(multiplier) * subStr)

        return "".join(stack)
