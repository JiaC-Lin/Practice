# Given an array of integers nums and an integer target, return INDICES of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Option 1: O(n^2) checking every number twice
        
        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

        # Option 2: O(n) hashmap checks in one pass by remembering the numbers visisted

        prevMap = {} # value : index
        for i, n in enumerate(nums): # enumerate = (index, num)
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i] # return [prevMap.get(diff), i]
            else: 
                prevMap[n] = i
        return


test = Solution()

nums1 = [2,7,11,15]
target1 = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums2 = [3,2,4]
target2 = 6
# Output: [1,2]

nums3 = [3,3]
target3 = 6
# Output: [0,1]

print(test.twoSum(nums1, target1))
print(test.twoSum(nums2, target2))
print(test.twoSum(nums3, target3))