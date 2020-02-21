/*
 * @lc app=leetcode.cn id=144 lang=swift
 *
 * [144] 二叉树的前序遍历
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
    func preorderTraversal(_ root: TreeNode?) -> [Int] {
        var result = [Int]()
        preorderTraversal(root, result: &result)
        return result
    }
    
    func preorderTraversal(_ node: TreeNode?, result: inout [Int]){
        guard let node = node else{
            return
        }
        result.append(node.val)
        preorderTraversal(node.left, result: &result)
        preorderTraversal(node.right, result: &result)
    }
}
// @lc code=end

