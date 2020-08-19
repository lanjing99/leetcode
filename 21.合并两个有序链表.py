#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = l1
        right = l2
        result: ListNode = ListNode()
        current = result
        
        while left and right:
            if left.val < right.val:
                current.next = left
                current = current.next
                left = left.next
            else:
                current.next = right
                current = current.next
                right = right.next

        if left:
            current.next = left
        else:
            current.next = right
        return result.next
# @lc code=end

