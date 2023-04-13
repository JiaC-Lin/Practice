# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Answer is guaranteed to be unique

from typing import List

class Solution(object):
# Option 1: using (num : count) as the dict. Fill in output with top k most frequent elements by initializing with k nums, then comparing down the list.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        countDict = {} # dict for numValue : count
        output = [0] * k # list to contain k most frequent elements
        
        # fill in countDict
        for n in nums:
            if n not in countDict: # skips recurring values; they're already counted
                value = nums.count(n)
                countDict[n] = value
        # print(f"{countDict}")

        lenK = k # save copy of k
        i = 0
        for key in countDict: # iterate through each numValue
            if k != 0: # fill/initialize in output up to k numValues
                output[i] = key 
                i += 1
                k -= 1
            else: # comparison for only the most frequent ones 
                for i in range(lenK):
                    numValue = output[i] # init and hold value
                    if countDict.get(numValue) < countDict.get(key):
                        output[i] = key
                        key = numValue
                        # Then continue to compare with the old numValue with the rest of the output array; countDict.get(numvalue) < countDict.get(oldNumValue)
        # print(f"{output}")
        return output
    
# Option 2: make a list of size N where the indexes will be the count and the elements will contain the element(s) with count equal to the index; runs in O(n)
    def neetTopKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = {} # (number: count)
        # make a list with size N (in case all numbers are same and highest count is N)
        freq = [[] for i in range(len(nums) + 1)] # index is going to be count and elements contains [number(s)]

        for n in nums: # count occurence of nums 
            count[n] = 1 + count.get(n, 0)
        # Flip dict and fill in the freq list
        for n, c in count.items():
            freq[c].append(n)
        # print(f"{freq}")

        output = []
        # decrement from len(freq) - 1 to 0 to get most frequent element, do it k times
        for i in range(len(freq) - 1, 0, -1): 
            for n in freq[i]:
                output.append(n)
                if len(output) == k: # stopping case
                    # print(f"{output}")
                    return output


test = Solution()

# k = 2, Output: [1,2]
num1 = [1, 1, 1, 2, 2, 3]

# k = 1, Output: [1]
num2 = [1]

# K = 2, Output: [5, 3]
num3 = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6]

test.topKFrequent(num1, 2)
test.topKFrequent(num2, 1)
test.topKFrequent(num3, 2)

test.neetTopKFrequent(num1, 2)
test.neetTopKFrequent(num2, 1)
test.neetTopKFrequent(num3, 2)