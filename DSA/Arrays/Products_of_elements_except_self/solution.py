'''Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
'''
from typing import List

def prod(self, arr):
        res = 1
        for element in arr:
            res*=element
        return res

def productExceptSelf(self, nums: List[int]) -> List[int]:
    
    left, right, result = [], [], []

    for i in range(len(nums)):
        left.append(self.prod(nums[:i]))
        right.append(self.prod(nums[i+1:]))

    for i in range(len(nums)):
        result.append(left[i]*right[i])

    return result