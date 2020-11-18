#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List

class Solution:
    columns = None
    rowIndex = None
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        #表示当前第n行对应的皇后在第几列
        self.columns = [0] * n 
        self.rowIndex = 0   #当前测试到第几行
        result = []
        # 第一行可以测试N个位置
        while self.columns[0] < n:
            # 当前这些位置是否可以放皇后们
            if self.canPutQueens():
                if self.rowIndex == n - 1:
                    result.append(self.queensMap(self.columns, n))
                    self.nextPosition(n)
                else:
                    self.rowIndex += 1  #从下一行开始寻找合适的位置
                    assert self.columns[self.rowIndex] == 0 # 新的一行从0开始验证
            else:
                self.nextPosition(n)
        return result            
                        
                
    def nextPosition(self, n):
        self.columns[self.rowIndex] += 1
        while  self.columns[self.rowIndex] == n and self.rowIndex > 0:
            if self.rowIndex != 0:      # line 18 用columns[0]来判断是否结束循环，所以不能设置为0，这不是个好的方法。待优化
                self.columns[self.rowIndex] = 0
            self.rowIndex -= 1
            self.columns[self.rowIndex] += 1 # 上一行的下一个位置
        
    def canPutQueens(self) -> bool:
        for i in range(0, self.rowIndex):
            # 因为已经在不同的行，所以不需要判断行
            # 是否在同一列
                if self.columns[self.rowIndex] == self.columns[i]:
                    return False
            #是否在对角线
                if self.rowIndex + self.columns[self.rowIndex] == i + self.columns[i]:
                    return False
                if self.rowIndex - self.columns[self.rowIndex] == i - self.columns[i]:
                    return False   
        return True
     
    def queensMap(self, columns: List[int], n: int) -> str:
        result = []
        for i in range(0, n):
            line = "." * columns[i] + "Q" + "." * (n - columns[i] - 1)
            result.append(line)
        return result
    
    
# result = Solution().solveNQueens(4)   
# print(result)          
# @lc code=end

