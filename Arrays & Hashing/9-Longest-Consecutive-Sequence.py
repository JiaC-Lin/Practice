# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time. So can't make it with sort due to O(nlogn)

from typing import List

class Solution(object):
# Go through list and get all the starting numbers of the sequences, then check using hashmap if the next number for each sequence is in it to add count. Then output the highest count from (first:count)
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        firstToCount = {}
        # get starting numbers as key of dict
        for n in nums:
            previous = n - 1
            if previous in nums: # not the first of a sequence
                continue
            else:
                firstToCount[n] = 1 # initialize the start of a sequence 
        # print(f"{firstToCount}")
        # count the number of elements for each sequence of starting nums
        for n, c in firstToCount.items():
            nextn = n + 1
            # if there is no next number; sequence ends -> loop exits
            while nextn in nums:
                c += 1 # add to count
                firstToCount[n] = c
                nextn += 1 # grab the number after nextn in the sequence
            # get largest sequence
            if c > output:
                output = c
        # print(f"{output}")
        # find highest num with highest count
        return output
    
# A more condensed solution
    def neetLongestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

nums1 = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

nums2 = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

test = Solution()

test.longestConsecutive(nums1)
test.longestConsecutive(nums2)