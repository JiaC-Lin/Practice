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
        print(f"{countDict}")

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
        print(f"{output}")
        return output
    
    def neetTopKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


test = Solution()

# k = 2, Output: [1,2]
num1 = [1, 1, 1, 2, 2, 3]

# k = 1, Output: [1]
num2 = [1]

# K = 2, Output: [2, 3]
num3 = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6]

test.topKFrequent(num1, 2)
test.topKFrequent(num2, 1)
test.topKFrequent(num3, 2)

test.neetTopKFrequent(num1, 2)
test.neetTopKFrequent(num2, 1)
test.neetTopKFrequent(num3, 2)