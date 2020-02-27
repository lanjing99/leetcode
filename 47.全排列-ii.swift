/*
 * @lc app=leetcode.cn id=47 lang=swift
 *
 * [47] 全排列 II
 */

// @lc code=start

//在排列之前提前剪枝，极大提高了效率， 48ms， 94.74%
class Solution {
    func permuteUnique(_ nums: [Int]) -> [[Int]] {
        let sortedNums = nums.sorted()
        var result = [[Int]]()
        func permuteUnique(prefix: [Int], remain: [Int]){
            guard remain.count > 1 else {
                var sum = prefix
                sum.append(contentsOf: remain)
                result.append(sum)
                return
            }
            
            for i in 0..<remain.count {
                //去除重复，因素nums排序过，所以只要和上一个比较即可。
                if i > 0 && remain[i] == remain[i - 1]{
                    continue
                }
                
                var nextRemain = remain
                nextRemain.remove(at: i)
                
                var nextPrefix = prefix
                nextPrefix.append(remain[i])
                permuteUnique(prefix: nextPrefix, remain: nextRemain)
    
            }
        }
        
        permuteUnique(prefix: [], remain: sortedNums)
        
        return result
    }
}


// //在结果中排除重复元素，效率比较差， 528ms， 10.43%
// class Solution {
//     func permuteUnique(_ nums: [Int]) -> [[Int]] {
//         var result = Set<[Int]>()
//         func permuteUnique(prefix: [Int], remain: [Int]){
//             guard remain.count > 1 else {
//                 var sum = prefix
//                 sum.append(contentsOf: remain)
//                 result.insert(sum)
//                 return
//             }
            
//             for i in 0..<remain.count {
//                 var nextRemain = remain
//                 nextRemain.remove(at: i)
                
//                 var nextPrefix = prefix
//                 nextPrefix.append(remain[i])
//                 permuteUnique(prefix: nextPrefix, remain: nextRemain)
    
//             }
//         }
        
//         permuteUnique(prefix: [], remain: nums)
        
//         return Array(result)
//     }
// }
// @lc code=end

