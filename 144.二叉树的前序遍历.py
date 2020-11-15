#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        if root is None:
            return result
        
        p = root
        while p is not None or len(stack) != 0:
            while p is not None:
                result.append(p.val)
                stack.append(p)
                p = p.left
                
            top = stack.pop()    
            p = top.right
            
        return result
    
# three = TreeNode(3)
# two = TreeNode(2, three, None)    
# one = TreeNode(1, None, two)

# print(Solution().preorderTraversal(one))  
# @lc code=end

