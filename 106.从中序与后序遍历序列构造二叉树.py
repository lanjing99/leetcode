#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        rootValue = postorder[-1]
        rootIndex = inorder.index(rootValue)
        leftInorder = inorder[0: rootIndex]
        leftPostorder = postorder[0: rootIndex]
        
        rightInorder = inorder[rootIndex+1: ]
        rightPostorder = postorder[rootIndex: -1]
        
        root = TreeNode(rootValue)
        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)
        return root
        
# @lc code=end

