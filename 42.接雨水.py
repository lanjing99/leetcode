#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from typing import List

# 使用栈解法
# 1. 栈单调递减
# 2. 判断左边界和右边界与面积的关系
class Solution:
    def trap(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i in range(0, len(heights)):
            while len(stack) != 0 and heights[i] > heights[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                w = i - stack[-1] - 1
                rightHeight = heights[i]
                leftHeight = heights[stack[-1]]
                h = 0
                if rightHeight < leftHeight:
                    h = rightHeight - heights[top]
                else:
                    h = leftHeight - heights[top]
                area += w * h
            stack.append(i)
        return area
# print(Solution().trap([4,2,0,3,2,5]))      
# @lc code=end

