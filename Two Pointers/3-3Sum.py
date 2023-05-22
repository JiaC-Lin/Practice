# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List

# 1  1  3  4  5  6  7  8  9 
# a [b                    c] 2sum with b and c
#       a  [b             c] 2sum with b and c while skipping duplicates with a
    
class Solution():
    # sort the array first to disallow repeats, make a nested loop where first loop is for number (a) and second loop is for 2sum using numbers (b) and (c)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        size = len(nums)
        for i in range(size):
            a = nums[i]
            # Skip any duplicates by checking if (a) is the same
            if ((i > 0) and (a == nums[i-1])):
                continue 
            # Set-Up 2sum
            b = i + 1       # start of 2sum after (a)
            c = size - 1    # end of 2sum
            target = 0 - a
            # Begin 2sum with b and c
            while b < c:
                total = nums[b] + nums[c]
                if total < target:
                    b += 1
                if total > target:
                    c -= 1
                # add solution to output and keep checking rest of nums
                if total == target:
                    output.append([a, nums[b], nums[c]])
                    b += 1
        # print(output)
        return output

test = Solution()

nums1 = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

nums2 = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

nums3 = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

test.threeSum(nums1)
test.threeSum(nums2)
test.threeSum(nums3)