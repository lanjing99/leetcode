/*
 * @lc app=leetcode.cn id=11 lang=swift
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var leftIndex = 0, rightIndex = height.count - 1
        
        var result = 0
        while rightIndex > leftIndex {
            let area = areaOfHeights(height, leftIndex: leftIndex, rightIndex: rightIndex)
            if area > result {
                result = area
            }
            
            //判断下一个可能的最大区域的一条边是左边还是右边
            if height[rightIndex] > height[leftIndex] {
                leftIndex += 1
            }else{
                rightIndex -= 1
            }
        }
        return result
    }
    
    //根据左边和右边的索引计算面积
    func areaOfHeights(_ heights: [Int], leftIndex: Int, rightIndex: Int) -> Int{
        var height = heights[leftIndex]
        if heights[rightIndex] < height {
            height = heights[rightIndex]
        }
        return (rightIndex - leftIndex) * height
    }
}
// @lc code=end

