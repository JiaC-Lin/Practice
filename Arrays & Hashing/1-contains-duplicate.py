# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List

class HashSet:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

nums1 = [1, 2, 3, 1] # True
nums2 = [1,2,3,4] # False
nums3 = [1,1,1,3,3,4,3,2,4,2] #True
test = HashSet()

print(test.containsDuplicate(nums1))
print(test.containsDuplicate(nums2))
print(test.containsDuplicate(nums3))
