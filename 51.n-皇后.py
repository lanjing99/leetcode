#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List

class Solution:  
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        self.dfs([], 0, n, result)
        return result
        
    def dfs(self, columns: List[int], rowIndex: int, n: int, result:List[str]):
        if rowIndex == n: #已经找到一个解了 rowIndex下标从0开始。
            result.append(self.queensMap(columns, n))
            return
        for i in range(0, n):
            if self.canPutQueens(columns, rowIndex, i):
                columnsCopy = columns[:]
                columnsCopy.append(i)
                self.dfs(columnsCopy, rowIndex + 1, n, result)
                

             
        
    def canPutQueens(self, columns: List[int], row: int, column: int) -> bool:
        assert len(columns) == row
        for i in range(0, row):
            # 因为已经在不同的行，所以不需要判断行
            # 是否在同一列
                if column == columns[i]:
                    return False
            #是否在对角线
                if row + column == i + columns[i]:
                    return False
                if row - column == i - columns[i]:
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

