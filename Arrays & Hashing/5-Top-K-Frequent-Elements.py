# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import List

class Solution(object):
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """


test = Solution()

# k = 2, Output: [1,2]
num1 = [1, 1, 1, 2, 2, 3]

# k = 1, Output: [1]
num2 = [1]

test.topKFrequent(num1, 2)
test.topKFrequent(num2, 1)