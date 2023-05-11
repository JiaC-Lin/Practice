# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution():
# Can use a stack to put in the opening parentisis and if met with a closing parentisis, pop out the opening parentisis if its the same type, otherwise return False; Return true if reached end of string and the stack is empty. O(n) for time and memory.
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for c in s:
            # Check if it's an opening and append into stack
            if (c == "(" or 
                c =="[" or 
                c == "{"):
                stack.append(c)
            # Check for statements where there is a closing before any opening is in stack
            elif (len(stack) == 0 and 
                  (c == ")" or c == "]" or c == "}")):
                print ("False")
                return False
            # Check if its closing AND at the top of stack then pop out of stack
            # If closing has no matching opening then it's not valid
            elif c == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    print("False")
                    return False
            elif c == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    print("False")
                    return False
            elif c == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    print("False")
                    return False
            
        # Check if there is a closing for every opening at the end for validity
        if len(stack) == 0:
            print("True")
            return True
        else:
            print("False")
            return False
        
# Condensed version using maps and not statements; only applies if the string only contains opening and closing pairs and nothing else
    def neetIsValid(self, s: str) -> bool:
        # Hashmap to map closing -> opening pairs
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            # check if c is not a closing, add c to stack
            if c not in Map:
                stack.append(c)
                continue
            # Invalid: if stack is empty (no opening elements) OR top element of stack does not match the mapped element of c (closing element do not match most recent opening)
            if not stack or stack[-1] != Map[c]:
                # print("False")
                return False
            # Valid: pop out the opening
            else: 
                stack.pop()

        # Return True if it's empty stack
        output = not stack
        # print(output)
        return output

# Condensed with maps and applies to all strings
    def isValid2(self, s: str) -> bool:
        map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            # Add opening elements to stack
            if (c == map[")"] or 
                c == map["]"] or 
                c == map["}"]):
                stack.append(c)
            # Skip any elements that's not closing or opening
            elif c not in map:
                continue
            # Check if c is a closing element in map and if stack is not empty first
            # Pop last element if map of closing matches the last element in stack
            elif ((c in map) and 
                  stack and 
                  (map[c] == stack[-1])):
                stack.pop()
            # Otherwise, stack is empty or closing element don't match most recent opening
            else:
                # print("False")
                return False
        
        # True if empty stack, False otherwise
        output = not stack
        # print("end:", output)
        return output

s1 = "(a)"
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

test.neetIsValid(s1)
test.neetIsValid(s2)
test.neetIsValid(s3)
test.neetIsValid(s4)

test.isValid2(s1)
test.isValid2(s2)
test.isValid2(s3)
test.isValid2(s4)