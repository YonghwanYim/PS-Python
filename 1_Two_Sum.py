"""
* Author : Yonghwan Yim
* LeetCode 1. Two Sum
* https://leetcode.com/problems/two-sum/description/
"""

# Brute force O(N^2)
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
