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
        i: int = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                break

            j = i + 1
            while j < len(nums) - 1:
                # 第一个数或者第一个数+第二个数大于0，提前退出
                if nums[i] + nums[j] > 0:
                    break
                # 跳过一组重复的数据
                if nums[j] == nums[j - 1] and j == i + 2:
                    i += 1
                    j += 1
                    continue

                if self.binarySearch(-nums[i] - nums[j], nums, j+1, len(nums)):
                    result.append([nums[i], nums[j], -nums[i] - nums[j]])
                
                j += 1

            i += 1
        return result

    def binarySearch(self, value: int, nums:List[int], start: int, end: int) -> bool:
        while start < end :
            middle: int = math.floor((start + end)/2)
            if value == nums[middle]:
                return True
            elif value > nums[middle]:
                start = middle + 1
            else: 
                end = middle
        return False

result = Solution().threeSum(nums=[-1,0,1,2,-1,-4])
print(result)
# @lc code=end

