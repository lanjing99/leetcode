#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None: 
            return False

        slowP = head
        fastP = head.next
        while slowP is not None:
            if slowP == fastP:
                return True
            elif fastP is None or fastP.next is None:
                break
            else:
                slowP = slowP.next
                fastP = fastP.next.next
        return False
        
# @lc code=end

