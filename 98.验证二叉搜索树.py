#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -sys.maxsize -1, sys.maxsize)
      
    def helper(self, root, minValue, maxValue) -> bool:
        # 把空节点和根节点点作为true返回
        if root is None: 
            return True 
        
        if root.val <= minValue or root.val >= maxValue:
            return False
        
        # 叶子节点，满足上面👆的条件后就为True
        if root.left is None and root.right is None:
            return True
        
        leftResult = self.helper(root.left, minValue, root.val)
        if leftResult == False:
            return False 
        
        rightResult = self.helper(root.right, root.val, maxValue)
        if rightResult == False:
            return False
        
        return True

# left = TreeNode(1)
# root = TreeNode(1)
# root.left = left
# Solution().isValidBST(root)
# @lc code=end

