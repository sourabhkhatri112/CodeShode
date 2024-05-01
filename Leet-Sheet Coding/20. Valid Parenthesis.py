'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
--> Open brackets must be closed by the same type of brackets.
--> Open brackets must be closed in the correct order.
--> Every close bracket has a corresponding open bracket of the same type.
'''

class Solution(object):
    def isValid(self, s):
        stack = []
        opening_brackets = ["(", "{", "["]

        if len(s) > 0 and len(s) <= 10000:
            print(len(s))
            for i in s:
                if i in opening_brackets:
                    stack.append(i)
                elif not stack and (i in ")" or i in "}" or i in "]"):
                    return False
                elif i == ")" and stack[::-1][0] == "(":
                    stack.pop()

                elif i == "}" and stack[::-1][0] == "{":
                    stack.pop()

                elif i == "]" and stack[::-1][0] == "[":
                    stack.pop()
                else:
                    return False

            if not stack:
                return True
        return False


print(Solution().isValid("()"))
