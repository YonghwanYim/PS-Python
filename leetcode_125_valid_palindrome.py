"""
* Author : Yonghwan Yim
* Final update : 25.07.28
* LeetCode 125. Valid Palindrome
* https://leetcode.com/problems/valid-palindrome/
"""

import collections
from typing import Deque
import re  # regular experssion; regex

class Solution_125(object): # 가장 기본적인 풀이 (Runtime : 7 ms)
    def isPalindrome(self, s : str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        strs = []
        for char in s:
            if char.isalnum():  # 영문, 숫자이면 true
                strs.append(char.lower())

        for i in range(len(strs) // 2):
            if strs[i] != strs[len(strs) - 1 - i]:
                return False

        # empty string은 당연히 palindrome
        return True

    def isPalindrome_1(self, s: str) -> bool: # using pop(), pop(0) (Runtime : 195 ms)
        """
        :type s: str
        :rtype: bool
        """
        strs = []
        for char in s:
            if char.isalnum():  # 영문, 숫자이면 true
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():  # 처음 값, 마지막 값을 pop으로 비교
                                           # pop(0)이 O(n)이라 느림. 반복하면 O(n^2)
                return False

        return True

    def isPalindrome_2(self, s: str) -> bool: # using Deque, popleft() (Runtime : 13 ms)
        """
        :type s: str
        :rtype: bool
        """
        # 자료형을 Deque로 선언 (pop이 빈번할 경우, list보다 deque를 사용하는 것이 효율적임)
        strs : Deque = collections.deque()
        for char in s:
            if char.isalnum():  # 영문, 숫자이면 true
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():  # 처음 값, 마지막 값을 pop으로 뺌.
                                              # popleft()는 O(1)이라 빠름. 반복하면 O(n)
                return False
        return True

    def isPalindrome_3(self, s:str) -> bool: # using Slicing (Runtime : 3 ms)
        strs = s.lower()
        # 정규식으로 숫자, 알파벳을 제외한 나머지는 필터링
        # re.sub(pattern, replacement, string)
        # 즉 맨 앞의 pattern에 해당되는 것들은 replacement에 들어가는 값으로 바꿈.
        strs = re.sub('[^a-z0-9]', '', strs)

        # strs[::-1]을 통해 뒤집은 문자열과 비교 (strs[::1]은 strs 원본과 동일)
        return strs == strs[::-1]


# test code
sol = Solution_125()
print(sol.isPalindrome_3('race a car'))
print(sol.isPalindrome_3('A man, a plan, a canal: Panama'))
print(sol.isPalindrome_3('  '))