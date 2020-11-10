#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i, height in enumerate(heights):
            # 计算左边的最大宽度
            left = i
            while left > 0 and heights[left - 1] >= height:
                left -= 1
            # 计算右边的最大宽度
            right = i
            while right < len(heights) - 1 and heights[right + 1] >= height:
                right += 1
            # 计算面积
            area = height * (right - left + 1)
            if area > maxArea:
                maxArea = area
        return maxArea
# @lc code=end

