# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation. This means naive brute force method won't work.

from typing import List

class Solution(object):
# Can be split into 2 arrays, one carrying the multiplication before nums[i] and one carrying multiplication after nums[i]
#    [ 1 , 2 , 3 , 4]       <- nums
# [1 , 1 , 2 , 6 , 24]      <- forward multiplcation -- one for loop
#    [ 24, 24, 12, 4 , 1] <- backward multiplcation -- second for loop
# answer[i] = forward[i] * backward[i + 1] -- third for loop
# O(3N + 2) or O(N) time
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        foward = [1] # make an array to hold foward multiplication
        for i in range(len(nums)):
            previousForward = foward[i]
            number = nums[i]
            multi = previousForward * number
            foward.append(multi)
        # print(f"{foward}")
        backward = [1] # make array to hold backward multiplication
        for i in range(len(nums) - 1, -1 , -1):
            previousBackward = backward[0]
            number = nums[i]
            multi = previousBackward * number
            # insert multi as first element and push everything back
            backward.insert(0, multi) 
        # print(f"{backward}")
        output = [] # make array for output as answer[i]
        for i in range(len(nums)):
            multi = foward[i] * backward[i + 1]
            output.append(multi)

        # print(f"{output}")
        return output
    
# Condensed Way -- will not include the last of 'foward' and first of 'backward' 
# [1 , 2 , 3 , 4] <- nums
# [1 , 1 , 2 , 6] <- forward multiplcation with 1 as prefix
# [24, 12, 4 , 1] <- backward multiplcation with 1 as postfix
# O(2N) or O(N)
    def neetProductExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i] # set next prefix to be added into answer array
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # backwards
            answer[i] *= postfix
            postfix *= nums[i] # set next postifx to be added into answer array
        return answer


test = Solution()

nums1 = [1,2,3,4]
# Output: [24,12,8,6]

nums2 = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

test.productExceptSelf(nums1)
test.productExceptSelf(nums2)

test.neetProductExceptSelf(nums1)
test.neetProductExceptSelf(nums2)