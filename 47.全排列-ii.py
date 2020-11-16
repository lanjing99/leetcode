#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper([], nums, result)
        return result
        
    def helper(self, prefix: List[int], remain: List[int], result: List[List[int]]):
        if len(remain) == 1:
            prefix.extend(remain)
            result.append(prefix)
            return 
        
        duplicateArray = []
        for value in remain:
            if duplicateArray.count(value) == 0:
                duplicateArray.append(value)
            else:
                continue
            
            prefixCopy = prefix.copy()
            prefixCopy.append(value)
            remainCopy = remain.copy()
            remainCopy.remove(value)
            self.helper(prefixCopy, remainCopy, result)
            
# array = [1]
# result = array.count(1)
# print(result)
# @lc code=end

