#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        
        stack = []
        current = root
        # 后续遍历，要等右节点访问后才能访问根节点，用lastVisited来区分右节点是否已经访问过了
        lastVisited = None   
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
        
            top = stack[-1]
            # 没有右子树，或者右子树已经访问过了
            if top.right is None or top.right == lastVisited:
                result.append(top.val)
                lastVisited = top
                stack.pop()
                current = None
            else:
                current = top.right
            
        return result
    
# @lc code=end

