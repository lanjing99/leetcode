#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.

# from typing import List

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            top = stack.pop()
            result.append(top.val)
            p = top.right
            
        
        return result
        
# three = TreeNode(3)
# two = TreeNode(2, three, None)    
# one = TreeNode(1, None, two)
# print(Solution().inorderTraversal(one))
# @lc code=end

