/*
 * @lc app=leetcode.cn id=88 lang=swift
 *
 * [88] 合并两个有序数组
 */

// @lc code=start
class Solution {
    func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
        var firstIndex = 0, secondIndex = 0
        while firstIndex < m + secondIndex && secondIndex < n {
            if nums1[firstIndex] > nums2[secondIndex] {
                moveOneStepRight(nums: &nums1, from: firstIndex, to: m+secondIndex)
                nums1[firstIndex] = nums2[secondIndex]
                secondIndex += 1
            }
            firstIndex += 1
        }
        
        while secondIndex < n {
            nums1[firstIndex] = nums2[secondIndex]
            firstIndex += 1
            secondIndex += 1
        }
    }
    
    func moveOneStepRight(nums : inout [Int], from: Int, to: Int){
        for i in ((from+1)...to).reversed(){
            nums[i] = nums[i - 1]
        }
    }
}

// @lc code=end

