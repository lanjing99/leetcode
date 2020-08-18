#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        current = 0
        lastNoZero = 0
        while current < len(nums):
            if nums[current] != 0:
                nums[lastNoZero] = nums[current]
                lastNoZero += 1
            current += 1

        while lastNoZero < len(nums):
            nums[lastNoZero] = 0
            lastNoZero += 1

        
# @lc code=end

