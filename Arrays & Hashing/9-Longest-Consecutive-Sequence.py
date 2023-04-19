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
        

nums1 = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

nums2 = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

test = Solution()

test.longestConsecutive(nums1)
test.longestConsecutive(nums2)