#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count: int = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[count]:
                count += 1
                nums[count] = nums[i]
        return count + 1

# @lc code=end

