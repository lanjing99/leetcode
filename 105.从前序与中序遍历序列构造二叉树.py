#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# from typing import List

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        if len(preorder) == 1:
            assert len(inorder) == 1
            return TreeNode(preorder[0])
        
        rootValue = preorder[0]
        root = TreeNode(rootValue)
        
        rootIndexInorder = inorder.index(rootValue)
        
        leftInOrder = inorder[0:rootIndexInorder]
        leftPreorder = preorder[1:rootIndexInorder + 1]
        root.left = self.buildTree(leftPreorder, leftInOrder)
        
        rightInOrder = inorder[rootIndexInorder + 1:]
        rightPreorder = preorder[rootIndexInorder + 1:]
        root.right = self.buildTree(rightPreorder, rightInOrder)

        return root
    
# result = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])        
# print(result)        
# @lc code=end

