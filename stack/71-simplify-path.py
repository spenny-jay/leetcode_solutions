# LINK: https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        # remove / characters (however all "/" are replaced with "")
        # ex: ["", "home", ""]
        names = path.split("/")
        stack = []
        for name in names:
            # if we encounter .., pop previous filename
            if name == "..":
                if stack: stack.pop()
            # ignore current directory and empty strings
            elif name != "." and name:
                stack.append(name)

        return "/" + "/".join(stack)