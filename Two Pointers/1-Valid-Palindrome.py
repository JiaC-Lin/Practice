# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution():
    # SAVE MEMORY, instead of creating a temporary holder for string, using an in-place method with POINTERS on left and right to check if alphanumerical elements are the same 1-by-1
    def isPalindrome(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Check if element is not alphanumerical, while within range, if not then move the pointer to the next element
            while (left < right) and (self.isAlphanumeric(s[left]) == False):
                left += 1
            while (left < right) and (self.isAlphanumeric(s[right]) == False):
                right -= 1
            # Stop if found fault with supposed palindrome; make letters to lowercase since we don't care about case
            if s[left].lower() != s[right].lower():
                print("False")
                return False
            left += 1
            right -= 1
        # True if we went through whole string and has no faults at being palindrome
        print("True")
        return True
        

    # implementation of isalnum() function to check if an element is either (A-Z), (a-z) or (0-9)
    def isAlphanumeric(self, c: chr) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        if (ord("A") <= ord(c) <= ord("Z") or 
            ord("a") <= ord(c) <= ord("z") or 
            ord("0") <= ord(c) <= ord("9")):
            return True
        else:
            return False
    
test = Solution()

s1 = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s2 = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

s3 = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

test.isPalindrome(s1)
test.isPalindrome(s2)
test.isPalindrome(s3)