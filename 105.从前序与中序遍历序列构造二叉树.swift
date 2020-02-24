/*
 * @lc app=leetcode.cn id=105 lang=swift
 *
 * [105] 从前序与中序遍历序列构造二叉树
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
    func buildTree(_ preorder: [Int], _ inorder: [Int]) -> TreeNode? {
        var preorderIndex = 0
        guard preorder.count > 0, inorder.count > 0, preorder.count == inorder.count else {
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
            
            //获取根节点
            let node = TreeNode.init(preorder[preorderIndex])
            //生成左右子树
            let rootIndex = map[preorder[preorderIndex]]!
            preorderIndex += 1
            node.left = buildTree(left: left, right: rootIndex)
            node.right = buildTree(left: rootIndex + 1, right: right)
            return node
        }
        
        return buildTree(left: 0, right: preorder.count)
        
    }
}
// @lc code=end

