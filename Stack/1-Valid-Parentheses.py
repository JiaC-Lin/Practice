# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution():
# Can use a stack to put in the opening parentisis and if met with a closing parentisis, pop out the opening parentisis if its the same type, otherwise return False; Return true if reached end of string and the stack is empty.
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            if (c == "(" or 
                c =="[" or 
                c == "{"):
                stack.append(c)
            elif c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                print("False")
                return False
        if len(stack) == 0:
            print("True")
            return True
        else:
            print("False")
            return False

s1 = "()"
# Output: true

s2 = "()[]{}"
# Output: true

s3 = "(]"
# Output: false

s4 = "([)]"
# Output: false

test = Solution()

test.isValid(s1)
test.isValid(s2)
test.isValid(s3)
test.isValid(s4)