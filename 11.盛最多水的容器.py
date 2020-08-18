#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            leftHeight = height[left]
            rightHeight = height[right]
            width = right - left
            area = 0
            if leftHeight < rightHeight:
                area = leftHeight * width
                left += 1
            else:
                area = rightHeight * width
                right -= 1

            if area > maxArea:
                maxArea = area
        return maxArea

# @lc code=end

