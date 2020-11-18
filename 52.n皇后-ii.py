#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    total = 0
    def totalNQueens(self, n: int) -> int:
        self.total = 0     
        self.dfs([], 0, n)
        return self.total
        
    def dfs(self, columns: List[int], rowIndex: int, n: int):
        if rowIndex == n: #已经找到一个解了 rowIndex下标从0开始。
            self.total += 1
            return
        for i in range(0, n):
            if self.canPutQueens(columns, rowIndex, i):
                columnsCopy = columns[:]
                columnsCopy.append(i)
                self.dfs(columnsCopy, rowIndex + 1, n)
                

             
        
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
     
# @lc code=end

