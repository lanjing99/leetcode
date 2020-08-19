#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
            
        result = head
        current = result.next
        result.next = None

        while current is not None:
            nextP = current.next
            current.next = result
            result = current
            current = nextP

        return result
        
# @lc code=end

