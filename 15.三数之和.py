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
        result :List[List[int]] = []
        nums.sort()
        target = 0
        listLength = len(nums)
        while target < listLength - 2:
            left = target + 1
            right = listLength - 1
            if nums[target] > 0:
                break
            
            # 去除重复的i
            if target > 0 and nums[target] == nums[target-1]:
                target += 1
                continue
            
            while left < right:
                #
                if left != target + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                
                if right != listLength - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                
                if nums[left] + nums[right] + nums[target] < 0:
                    left += 1

                elif nums[left] + nums[right] + nums[target] > 0:
                    right -= 1
                    
                else:
                    result.append([nums[target], nums[left], nums[right]])
                    left += 1
                    right -= 1
       
            target += 1   
        return result

print (Solution().threeSum([-1,0,1,2,-1,-4]))

# @lc code=end

