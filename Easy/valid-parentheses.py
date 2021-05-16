#  https://leetcode.com/problems/valid-parentheses/

class Solution:

    def isValid(self, s: str) -> bool:

        def is_pair(prev, cur):
            if prev == "(" and cur == ")":
                return True
            elif prev == "[" and cur == "]":
                return True
            elif prev == "{" and cur == "}":
                return True
            else:
                return False

        opens = ["(", "[", "{"]
        closes = [")", "]", "}"]

        stack = [" "]

        for b in s:
            if b in opens:
                stack.append(b)
            elif b in closes:
                if is_pair(stack[-1], b):
                    stack.pop()
                else:
                    return False
        if len(stack) == 1:
            return True
        else:
            return False

#####################################################################

sln = Solution()
res = sln.isValid("[({})]")
print(res)