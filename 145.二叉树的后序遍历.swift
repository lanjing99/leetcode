/*
 * @lc app=leetcode.cn id=145 lang=swift
 *
 * [145] 二叉树的后序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */
class Solution {
    func postorderTraversal(_ root: TreeNode?) -> [Int] {
        var result = [Int]()
        postorderTraversal(root, result: &result)
        return result
    }
    
    func postorderTraversal(_ node: TreeNode?, result: inout [Int]){
        guard let node = node else{
            return
        }
        
        postorderTraversal(node.left, result: &result)
        postorderTraversal(node.right, result: &result)
        result.append(node.val)
    }
}
// @lc code=end

