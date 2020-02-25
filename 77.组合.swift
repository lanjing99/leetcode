/*
 * @lc app=leetcode.cn id=77 lang=swift
 *
 * [77] 组合
 */

// @lc code=start
//1. 弄清楚 N 和 N-1 之间的关系，这里要求的组合是不重复的。返回条件是k==1的时候
//2. 注意小标， startIndex从1开始，而不是从0， 判断条件是tartIndex <= n - count + 1， 用特殊值试一下。例如4 2
class Solution {
    func combine(_ n: Int, _ k: Int) -> [[Int]] {
        var result = [[Int]]()
        
        func combine(prefix: [Int], start: Int, count: Int){
            guard count > 1 else {
                for i in start...n {
                    var value = prefix
                    value.append(i)
                    result.append(value)
                }
                return
            }
            
            var startIndex = start
            while startIndex <= n - count + 1{
                var nextPrefix = prefix
                nextPrefix.append(startIndex)
                combine(prefix: nextPrefix, start: startIndex + 1, count: count - 1)
                startIndex += 1
            }
            
        }

        combine(prefix: [], start: 1, count: k)
        return result
    }
}
// @lc code=end

