/*
 * @lc app=leetcode.cn id=46 lang=swift
 *
 * [46] 全排列
 */

// @lc code=start
class Solution {
    func permute(_ nums: [Int]) -> [[Int]] {
        var result = [[Int]]()
        func permute(prefix: [Int], remain: [Int]){
            guard remain.count > 1 else {
                var sum = prefix
                sum.append(contentsOf: remain)
                result.append(sum)
                return
            }
            
            for i in 0..<remain.count {
                var nextRemain = remain
                nextRemain.remove(at: i)
            
                var nextPrefix = prefix
                nextPrefix.append(remain[i])
                permute(prefix: nextPrefix, remain: nextRemain)
            }
        }
        
        permute(prefix: [], remain: nums)
        
        return result
    }
}
// @lc code=end

