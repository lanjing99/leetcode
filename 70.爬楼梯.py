#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        previos = 0
        current = 1
        for _ in range(0, n):
            current, previos = current + previos, current
        return current
# @lc code=end

