# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

from typing import List

class Solution():
# Since list is sorted, we can solve in linear time and constant space without a nested for loop by having pointers for smallest and biggest
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        small = 0
        big = len(numbers) - 1

        while small < big:
            added = numbers[small] + numbers[big] 
            if added == target:
                print([small + 1, big + 1])
                return [small + 1, big + 1]
            if added > target: # too big
                big -= 1
            if added < target: # too small
                small += 1
        return False

numbers1 = [2,7,11,15]
target1 = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

numbers2 = [2,3,4]
target2 = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

numbers3 = [-1,0]
target3 = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

test = Solution()

test.twoSum(numbers1, target1)
test.twoSum(numbers2, target2)
test.twoSum(numbers3, target3)