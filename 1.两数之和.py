#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, value in enumerate(nums):
            if map.get(target - value) is not None:
                return [map.get(target - value), i]
            else:
                map[value] = i
        return [0, 0]
# Solution().twoSum(nums= [2,7,11,15], target= 9)
# @lc code=end

