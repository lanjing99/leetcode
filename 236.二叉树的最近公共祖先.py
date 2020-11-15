#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left is None:
            return right
        if right is None:
            return left

# left = TreeNode(5)
# right = TreeNode(1)
# root = TreeNode(3)
# root.left = left
# root.right = right 

# ancestor = Solution().lowestCommonAncestor(root, left, right)
# print(ancestor.val)     
# @lc code=end

# from enum import Enum
# class Status(Enum):
#     NotFound = 0
#     FoundOne = 1
#     FoundTwo = 2
    
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         status, ancestor = self.helper(root, p, q)
#         assert status == Status.FoundTwo
#         return ancestor
    
#     # 返回一个元组，
#     def helper(self, node, p, q):
#         if node is None:
#             return (Status.NotFound, None)
        
#         leftStatus, leftAncestor = self.helper(node.left, p, q)
#         rightStatus, rightAncestor = self.helper(node.right, p, q)
        
#         if leftStatus == Status.FoundTwo:
#             return (leftStatus, leftAncestor)
#         if rightStatus == Status.FoundTwo:
#             return (rightStatus, rightAncestor)
        
#         if leftStatus == Status.FoundOne and rightStatus == Status.FoundOne :
#             return (Status.FoundTwo, node)
        
#         if leftStatus == Status.FoundOne or rightStatus == Status.FoundOne :
#             if node == p or node == q :
#                 return (Status.FoundTwo, node)
#             else:
#                 return (Status.FoundOne, None)
        
#         if node == p or node == q :
#             return (Status.FoundOne, None)
#         else:
#             return (Status.NotFound, None)