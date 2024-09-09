#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# NeetCode Practice
# Anagram Groups (Easy)
from typing import List
class Solution:
    def hasDuplicate(nums: List[int]) -> bool: 
        num_hash = {}
        for i in nums:
            if i not in num_hash:
                num_hash[i] = 1
            else:
                num_hash[i] += 1

        if any(value > 1 for value in num_hash.values()):
            print("True")
            return True 
        else:
            print("False")
            return False 
    hasDuplicate([1, 2, 3, 4, 5, 6])