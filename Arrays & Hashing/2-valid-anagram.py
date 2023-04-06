# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # O(S + T) in time and memory 

        if len(s) != len(t):
            return False

        countS = dict()
        countT = dict()

        for n in range(len(s)):
            countS[s[n]] = 1 + countS.get(s[n], 0)
            countT[t[n]] = 1 + countT.get(t[n], 0)
        print(countS)
        if countS == countT:
            return True
        else:
            return False 

        # O(nlogn) in time and O(1) in memory
    
        return sorted(s) == sorted(t)

test = Solution()

s1 = "anagram"
t1 = "nagaram" # True

s2 = "rat"
t2 = "car" # False

print(test.isAnagram(s1, t1))
print(test.isAnagram(s2, t2))