/*
 * @lc app=leetcode.cn id=70 lang=swift
 *
 * [70] 爬楼梯
 */

// @lc code=start
class Solution {
    func climbStairs(_ n: Int) -> Int {
        guard n != 1 else {
            return 1
        }
        guard n != 2 else {
            return 2
        }
        
        var previos = 1, result = 2
        for i in 3...n {
            let temp = previos + result
            previos = result
            result = temp
        }
        return result
    }
}
// @lc code=end

