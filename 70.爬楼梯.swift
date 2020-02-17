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
        
        guard n != 2 else{
            return 2
        }
        
        return climbStairs(n-1) + climbStairs(n-2)
    }
}
// @lc code=end

