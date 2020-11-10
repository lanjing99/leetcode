#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start

from typing import List
from collections import deque

class Solution:
    q = deque()
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if k == 0 or len(nums) < k:
            return result
        
        for i in range(0, k):
            self.addToQueue(nums, i, k)
        result.append(nums[self.q[0]])    
        
        for i in range(k, len(nums)):
            self.addToQueue(nums, i, k)
            result.append(nums[self.q[0]])
        
        return result
    
    def addToQueue(self, nums, index, k):
        # 超过滑动窗口
        if len(self.q) != 0 and index - self.q[0] == k:
            self.q.popleft()
        
        # 去除比当前值小的值
        while len(self.q) != 0 and nums[index] > nums[self.q[-1]]:
            self.q.pop()
            
        self.q.append(index)
        return
    
print(Solution().maxSlidingWindow([1], 1))
# @lc code=end

