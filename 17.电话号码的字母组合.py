#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == "":
            return result
        
        digitString = {"2":"abc",
                       "3":"def",
                       "4":"ghi", 
                       "5":"jkl", 
                       "6":"mno",
                       "7":"pqrs", 
                       "8":"tuv", 
                       "9":"wxyz"}
        letters = []
        for digit in digits:
            letters.append(digitString[digit])
            
        self.helper("", letters, result)
        return result
    
    def helper(self, prefix:str, letters:List[str], result:List[str]):
        if len(letters) == 0:
            result.append(prefix)
            return
        
        for letter in letters[0]:
            self.helper(prefix + letter, letters[1:], result)
        
result = Solution().letterCombinations("")
print(result)        
# @lc code=end

