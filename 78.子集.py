#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper([], nums, result)
        return result
        
    def helper(self, prefix:List[int], remain:List[int], result:List[List[int]]):
        if len(remain) == 0:
            result.append(prefix)
            return
        
        prefixCopy = prefix.copy()
        prefixCopy.append(remain[0])
        self.helper(prefixCopy, remain[1:], result)
        
        self.helper(prefix, remain[1:], result)
# @lc code=end

