#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'}':'{',
               ']':'[',
               ')':'('}
        
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != dic[c]:
                    return False 
                
        if len(stack) == 0:
            return True
        else:
            return False    
        
# print(Solution().isValid("{[]})"))
# @lc code=end

