#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        
        result = []
        self.helper([], n, k, result)
        return result
        
    def helper(self, prefix:List[int], n: int, k: int, result: List[List[int]]):
        if k == 0:
            result.append(prefix)
            return
        if n == 0:
            return 
        
        copy2 = prefix.copy()
        copy2.append(n)
        self.helper(copy2, n - 1, k-1, result)
        
        copy1 = prefix.copy()
        self.helper(copy1, n - 1, k, result)
        
result = Solution().combine(4, 2)        
print(result)
# @lc code=end

