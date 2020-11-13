#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    result = []
    count = 0
    def generateParenthesis(self, n: int) -> List[str]:
        self.count = n
        self.result = []
        self.helper("", 0, 0)
        return self.result
        
    def helper(self, partResult:str, left:int, right:int):
        if left == self.count and right == self.count:
            self.result.append(partResult)
            return
        
        if left < self.count:
            self.helper(partResult + "(", left + 1, right)
        if right < left and right < self.count:
            self.helper(partResult + ")", left, right + 1)
        
# @lc code=end

