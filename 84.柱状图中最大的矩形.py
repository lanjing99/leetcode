#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from typing import List
import sys

class Solution:
    stack = [(-1, 0)] 
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
         # 存放元素，第一个元素是数组下标，第二个元素是高度
        for rightBound, height in enumerate(heights):
            # 当前高度和栈顶位置相比
            if height >= self.stack[-1][1]:
                self.stack.append((rightBound, height))
            else:
                area = self.areaWithRightElement(rightBound, height) 
                self.stack.append((rightBound, height)) 
                if area > result:
                    result = area
        
        # 处理栈中剩余的元素
        while len(self.stack) > 1:
            area = self.areaWithRightElement(len(heights), 0)
            if area > result:
                result = area 
           
        return result
    
    def areaWithRightElement(self, rightBound, height):
        result = 0
        # 当前高度小于栈顶高度，当前就是右边界，左边界是栈顶的上一个元素
        # 要一直pop比当前高度大的值
        top = self.stack[-1]  #获取顶部的高度
        if top[1] <= 0:
            self.stack.pop()
            return 0
        
        while height < top[1]:
            topHeight = top[1]   
            self.stack.pop()
            previous = self.stack[-1]
            leftBound = previous[0]
            # rightBound = top.[0]
            area = topHeight * (rightBound - leftBound - 1)
            if area > result:
                result = area
                
            top = previous
             
        return result 
    
# print(Solution().largestRectangleArea([0]))
# @lc code=end

