"""
* Author : Yonghwan Yim
* Final update : 25.07.28
* LeetCode 344. Reverse String
* https://leetcode.com/problems/reverse-string/description/
"""

from typing import List

class Solution:
    """
    Do not return anything, modify s in-place instead.
    You must do this by modifying the input array in-place with O(1) extra memory.
    """
    def reverseString(self, s: List[str]) -> None: # 가장 기본적인 방식 (Runtime : 3 ms)
        for i in range(len(s)//2):
            temp = s[-(i+1)]
            s[-(i+1)] = s[i]
            s[i] = temp

    def reverseString_1(self, s: List[str]) -> None: # using Two Pointer (Runtime : 3 ms)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString_2(self, s : List[str]) -> None: # Pythonic way. using reverse() (Runtime : 0 ms)
        s.reverse()  # list 뒤집으면 끝

