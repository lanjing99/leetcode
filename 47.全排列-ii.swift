/*
 * @lc app=leetcode.cn id=47 lang=swift
 *
 * [47] 全排列 II
 */

// @lc code=start
class Solution {
    func permuteUnique(_ nums: [Int]) -> [[Int]] {
        var result = Set<[Int]>()
        func permuteUnique(prefix: [Int], remain: [Int]){
            guard remain.count > 1 else {
                var sum = prefix
                sum.append(contentsOf: remain)
                result.insert(sum)
                return
            }
            
            for i in 0..<remain.count {
                var nextRemain = remain
                nextRemain.remove(at: i)
                
                var nextPrefix = prefix
                nextPrefix.append(remain[i])
                permuteUnique(prefix: nextPrefix, remain: nextRemain)
    
            }
        }
        
        permuteUnique(prefix: [], remain: nums)
        
        return Array(result)
    }
}
// @lc code=end

