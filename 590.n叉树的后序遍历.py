#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, node, result):
        if node is None:
            return
        
        for child in node.children:
            self.helper(child, result)
        result.append(node.val)
        
# @lc code=end

