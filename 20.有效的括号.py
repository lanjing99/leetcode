#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                
                if c == ')':
                   top = stack.pop()
                   if top != '(':
                       return False
                elif c == ']':
                    top = stack.pop()
                    if top != '[':
                        return False
                else:
                # c == '}':
                    top = stack.pop()
                    if top != '{':
                        return False
        if len(stack) == 0:
            return True
        else:
            return False    
        
# print(Solution().isValid("{[]})"))
# @lc code=end

