#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums, start= 0, end= len(nums))
        self.reverse(nums, start=0, end=k)
        self.reverse(nums, start=k, end=len(nums))

    def reverse(self, nums: List[int], start:int, end: int):
        left = start
        right = end - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    

                
# @lc code=end

