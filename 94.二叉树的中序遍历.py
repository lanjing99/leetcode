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
        
        stack = [root]
        current = root
       
        while current is not None or len(stack) != 0:
            while current is not None and current.left is not None:
                stack.append(current.left)
                current = current.left
    
            current = stack.pop()
            result.append(current.val)
            current = current.right
            if current is not None:
                stack.append(current)

        return result
        
# three = TreeNode(3)
# two = TreeNode(2, three, None)    
# one = TreeNode(1, None, two)
# print(Solution().inorderTraversal(one))
# @lc code=end

