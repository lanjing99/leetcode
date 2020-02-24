/*
 * @lc app=leetcode.cn id=106 lang=swift
 *
 * [106] 从中序与后序遍历序列构造二叉树
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
    func buildTree(_ inorder: [Int], _ postorder: [Int]) -> TreeNode? {
        var postorderIndex = postorder.count
        guard postorder.count > 0, inorder.count > 0, postorder.count == inorder.count else {
            return nil
        }
        
        var map = [Int: Int]()
        for i in 0..<inorder.count{
            map[inorder[i]] = i
        }
        
        
        
        func buildTree(left: Int, right: Int) -> TreeNode?{
            guard left < right else {
                return nil
            }
            
            postorderIndex -= 1
            //获取根节点
            let node = TreeNode.init(postorder[postorderIndex])
            //生成左右子树
            let rootIndex = map[postorder[postorderIndex]]!
            
            node.right = buildTree(left: rootIndex + 1, right: right)
            node.left = buildTree(left: left, right: rootIndex)       
            return node
        }
        
        return buildTree(left: 0, right: inorder.count)
    }
}
// @lc code=end

