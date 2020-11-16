#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper([], nums, result)
        return result
        
    def helper(self, prefix: List[int], remain: List[int], result: List[List[int]]):
        if len(remain) == 1:
            prefix.extend(remain)
            result.append(prefix)
            return 
        
        for value in remain:
            prefixCopy = prefix.copy()
            prefixCopy.append(value)
            remainCopy = remain.copy()
            remainCopy.remove(value)
            self.helper(prefixCopy, remainCopy, result)
            
# @lc code=end

