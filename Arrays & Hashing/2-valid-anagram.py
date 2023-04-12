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
            # increment character by one everytime we see it with the default value for key to be 0; countS[s[n]] += 1 with countS[s[n]] initialzed with 0
            countS[s[n]] = 1 + countS.get(s[n], 0)
            countT[t[n]] = 1 + countT.get(t[n], 0)
        print(countS, countT)

        if countS == countT: # compare the letter counts, with dict, in both words
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