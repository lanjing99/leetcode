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
        result = []
        if root is None:
            return result
        
        # result.append(root.val)
        stack = []
        current = root
        
        while len(stack) > 0 or current is not None:
            # 遍历左子树        
            while current is not None:
                        result.append(current.val)
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            
            if current.right is not None:
                current = current.right
            else:
                current = None
    
        return result
    
# three = TreeNode(3)
# two = TreeNode(2, three, None)    
# one = TreeNode(1, None, two)

# print(Solution().preorderTraversal(one))  
# @lc code=end

