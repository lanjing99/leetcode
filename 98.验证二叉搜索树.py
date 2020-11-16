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
        # return self.helper(root, -sys.maxsize -1, sys.maxsize)
        if root is None:
            return True
        
        # 保存一个节点的状态，当前根节点，当前子树的最小值，最大值
        stack = [] 
        p = root
        min = -sys.maxsize -1
        max = sys.maxsize
        
        while p or stack:
            while p:
                if self.isValidateNode(p, min, max) == False:
                    return False
                  
                stack.append((p, min, max))
                max = p.val
                p = p.left
            
            top = stack.pop()
            min = top[0].val
            max = top[2]
            p = top[0].right    
                
        return True       
                
     
    def isValidateNode(self, node: TreeNode, min: int, max: int) -> bool:
        assert node
        return node.val > min and node.val < max

    

# left = TreeNode(1)
# right = TreeNode(3)
# root = TreeNode(2)
# root.left = left
# root.right = right
# Solution().isValidBST(root)
# @lc code=end

