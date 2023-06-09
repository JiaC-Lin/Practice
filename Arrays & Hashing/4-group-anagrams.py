# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from typing import List
from collections import defaultdict

class Solution(object):
# Option 1: Sort the words then compare them and pull the originals that are anagrams with each other into a group
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = []
        # Create a new list, using list comprehension, with each word sorted
        sorted_list = [''.join(sorted(word)) for word in strs]
        
        # Compare and group anagrams together without repeats
        N = len(strs)
        # initialize a skip array to skip elements that are added to output already
        skip = [] 
        for i in range(N):
            if i in skip:
                continue # skips the element if its in output
            group = [strs[i]] # initialize a group array to group anargams
            for j in range(i + 1, N):
                # Compares each element in sorted_list to see if they are anagrams
                if sorted_list[i] == sorted_list[j]:
                    skip.append(j) # add element to skip so it won't repeat
                    group.append(strs[j]) # add element to group if anagram
            
            # Put the group of anagram into a list; all the anagram groups are in a single list
            output.append(group)

        return output
    
# Option 2: Using dict to group the words that are sorted on the spot. Then put all the values in a list.
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {} 
        # Sort each word one by one and put them in a dictionary, as the keys, if they aren't already then with sorted word as key add words that are anagrams as the value.
        for word in strs: 
            sorted_word = ''.join(sorted(word))
            # If there is no key for sorted word yet, initialize it with word
            if sorted_word not in dictionary:
                dictionary[sorted_word] = [word]
            # Else add word to dict of sorted word
            else:
                dictionary[sorted_word].append(word)
            # print(f"{dictionary}")
                
        # Put in anagram values from dict to a list for output
        output = []
        for value in dictionary.values():
            output.append(value)
        return output
        

# Option 3: Create hashmap, using defaultdict and tuple, with key being the COUNT for each letter and value being the words that are anagrams with the same count for each letter
    def neetGroupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = defaultdict(list) # charCount : list of anagrams

        for word in strs:
            count = [0] * 26 # count for each char a .. z
            for char in word:
                # increment index based on letter for the word
                count[ord(char) - ord("a")] += 1 
            # use tuple to store the list as a key value then append word as value to the defaultdict
            output[tuple(count)].append(word)

        # only need the values of the default dict
        return output.values()
            
        
test = Solution()

strs1 = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs2 = [""]
# Output: [[""]]

strs3 = ["a"]
# Output: [["a"]]

print(test.groupAnagrams(strs1))
print(test.groupAnagrams(strs2))
print(test.groupAnagrams(strs3), end="\n\n")
print(test.groupAnagrams2(strs1))
print(test.groupAnagrams2(strs2))
print(test.groupAnagrams2(strs3), end ="\n\n")
print(test.neetGroupAnagrams(strs1))
print(test.neetGroupAnagrams(strs2))
print(test.neetGroupAnagrams(strs3), end="\n\n")