#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if root is None:
            return result
        
        q = deque([root])
        while q:
            level = []
            levelLength = len(q)
            for i in range(0, levelLength):
                node = q.popleft()
                level.append(node.val)
                for child in node.children:
                    if child is not None:
                        q.append(child)
            result.append(level)
            
        return result
        
# @lc code=end

