#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordsQueue = deque([beginWord])
        remainsQueue = deque(wordList)
        tempQueue = deque()
        len1 =len(wordsQueue)
        len2 = len(wordList)
        
        if wordList.count(endWord) == 0:
            return 0
        
        length = 1
        while wordsQueue:
            levelLength = len(wordsQueue)
            while levelLength > 0:
                levelLength -= 1
                
                word = wordsQueue.popleft()
                beforeRemoveLength = len(remainsQueue)
                while remainsQueue:
                    compareWord = remainsQueue.popleft()
                    diffCount = self.letterDifferentCount(word, compareWord)
                    if diffCount == 1:
                        wordsQueue.append(compareWord)
                        if compareWord == endWord:
                            return length + 1
                    elif diffCount != 0 :  #去除相同的元素
                        tempQueue.append(compareWord)
                
                # # 没有找到任何一个相差为1的词，说明找不到转换路径        
                # if beforeRemoveLength == len(tempQueue):
                #     return 0
                
                remainsQueue = tempQueue
                tempQueue = deque()
            length += 1
        return 0    
                
                
    def letterDifferentCount(self, first:str, second: str) -> int:
        assert len(first) == len(second)
        result = 0
        for i in range(0, len(first)):
            if first[i] != second[i]:
                result += 1
        return result
                   
# result = Solution().ladderLength("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"])     
# print(result)        
        
# @lc code=end

