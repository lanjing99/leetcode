#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1
        leftMaxHeight = 0
        rightMaxHeight = 0
        while left < right:
            while heights[left] <= heights[right]:
                if left == right:
                    break
                
                if heights[left] < leftMaxHeight:
                    area += leftMaxHeight - heights[left]
                else:
                    leftMaxHeight = heights[left]
                left += 1
            while heights[right] < heights[left]:
                # if left == right:
                #     break
                
                if heights[right] < rightMaxHeight:
                    area += rightMaxHeight - heights[right]
                else:
                    rightMaxHeight = heights[right]
                right -= 1
                
        return area



# # 使用栈解法
# # 1. 栈单调递减
# # 2. 判断左边界和右边界与面积的关系
# class Solution:
#     def trap(self, heights: List[int]) -> int:
#         stack = []
#         area = 0
#         for i in range(0, len(heights)):
#             while len(stack) != 0 and heights[i] > heights[stack[-1]]:
#                 top = stack.pop()
#                 if len(stack) == 0:
#                     break
#                 w = i - stack[-1] - 1
#                 rightHeight = heights[i]
#                 leftHeight = heights[stack[-1]]
#                 h = 0
#                 if rightHeight < leftHeight:
#                     h = rightHeight - heights[top]
#                 else:
#                     h = leftHeight - heights[top]
#                 area += w * h
#             stack.append(i)
#         return area
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))      
# @lc code=end

