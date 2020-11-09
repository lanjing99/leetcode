#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
import math

# @lc code=start
class MinStack:
    

    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]


    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        x = self.stack.pop()
        assert x >= self.min_stack[-1]
        if x == self.min_stack[-1]:
            self.min_stack.pop()
        return x

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

