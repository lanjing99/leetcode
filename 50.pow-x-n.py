#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        
        half = n // 2
        halfResult = self.myPow(x, half)
        if n % 2 == 0:
            return halfResult * halfResult
        else: 
            return halfResult * halfResult * x
        
# Solution().myPow(2.0, 10)
# @lc code=end

