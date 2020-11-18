#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        result = []
        while len(queue):
            maxValue = - sys.maxsize
            length = len(queue)
            while length > 0:
                length -= 1
                node = queue.popleft()
                if node.val > maxValue:
                    maxValue = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(maxValue)
        return result
        
# @lc code=end

