/*
 * @lc app=leetcode.cn id=107 lang=swift
 *
 * [107] 二叉树的层次遍历 II
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?q
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
 //1. Swift Array 是个值类型，有时候也挺麻烦的，要先取出数组，修改，然后再复制改回去
 //2. level信息当做参数来传递
class Solution {
    func levelOrderBottom(_ root: TreeNode?) -> [[Int]] {
        var result = [[Int]]()
        func levelOrderBottom(node: TreeNode?, level: Int){
            guard let node = node else {
                return
            }
            if result.count == level {
                result.append([Int]())
            }
            var nodesAtLevel = result[level]
            nodesAtLevel.append(node.val)
            result[level] = nodesAtLevel
            
            levelOrderBottom(node: node.left, level: level + 1)
            levelOrderBottom(node: node.right, level: level + 1)
            
        }
        
        levelOrderBottom(node: root, level: 0)
        return result.reversed()
    }
}
// @lc code=end

