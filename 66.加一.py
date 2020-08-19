#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits), 0, -1):
            digits[i - 1] += 1
            if digits[i - 1] == 10:
                digits[i - 1] = 0
            else:
                break

        if digits[0] == 0:
            digits.insert(0, 1)
        return digits
# @lc code=end

