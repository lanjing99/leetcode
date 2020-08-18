#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List
import math

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result: List[List[int]] = []
        numsLen = len(nums)
        for i in range(0, numsLen - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = numsLen - 1
            while left < right:
                # 去除左边的重复
                if left != i+1 and nums[left] == nums[left -1]:
                    left += 1
                    continue
                # 去除右边的重复
                if right != numsLen - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue 

                if -nums[i] == nums[left] + nums[right]:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                elif -nums[i] > nums[left] + nums[right]:
                    left += 1
                else:
                    right -= 1

        return result


# @lc code=end

