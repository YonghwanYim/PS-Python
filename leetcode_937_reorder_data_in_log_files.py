"""
* Author : Yonghwan Yim
* Final update : 25.08.01
* LeetCode 937. Reorder Data in Log Files
* https://leetcode.com/problems/reorder-data-in-log-files/description/
"""
from typing import List

class Solution: # runtime : 2 ms
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []   # empty list
        for log in logs: # letter, digit의 두 타임을 먼저 나눔
            if log.split()[1].isdigit():  # spilt 후 두 번째 요소를 가져옴 ([1] <- 이 인덱스 의미)
                digits.append(log)
            else:
                letters.append(log)

        # lambda로 간단하게 표현. identifier를 제외하고 비교. 같으면 identifier을 기준으로 정렬.
        letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))   # x.split()[0] means identifier
        return letters + digits

# Example
logs1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
logs2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

# Test
sol = Solution()
print(sol.reorderLogFiles(logs1))
print(sol.reorderLogFiles(logs2))





