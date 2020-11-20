#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from collections import deque
from collections import defaultdict
from typing import List

# 参考官方题解实现
# https://leetcode-cn.com/problems/word-ladder/solution/dan-ci-jie-long-by-leetcode-solution/
class Solution:
    wordIDDic = dict()
    nodeCount = 0
    edges = None # 是字典，下标是节点的编号，值以相邻的边的数组
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.wordIDDic = dict()
        self.nodeCount = 0
        # 这个意思是创建一个字典，value如果没有值的话，默认值是list类型的[],确实挺方便的。
        # 但是感觉Python的这些语法糖很细碎
        self.edges = defaultdict(list)  
        
        # 添加词语，构建一个word的图结构
        for word in wordList:
            self.addWord(word)
        
        # # for test only
        # idWordDic = {value: key for key, value in  self.wordIDDic.items()}
        # for key in idWordDic:
        #     print(idWordDic[key] + " : ", end = "")
        #     for node in self.edges[key]:
        #         print(idWordDic[node] + ",", end = "")
        #     print("")
       
        # distance[node] 表示 node节点到beginword节点的距离
        # 要有distance[] 数据，因为图是双向，否则层级遍历的时候，会回到父节点
        
        self.addWord(beginWord)
        distance = [float("inf")] * self.nodeCount  
        distance[self.wordIDDic[beginWord]] = 0
        
        
        if endWord not in self.wordIDDic:
            return 0
        
        wordQueue = deque([self.wordIDDic[beginWord]])
        level = 1
        while wordQueue:
            levelLength = len(wordQueue)
            while levelLength > 0:
                levelLength -= 1 
                wordID = wordQueue.popleft()

                if wordID == self.wordIDDic[endWord]:
                    return (level // 2) + 1
            
                for x in self.edges[wordID]:
                    if distance[x] == float("inf"):
                        distance[x] = level
                        wordQueue.append(x)
            level += 1
        return 0  
           
    # 一个word是一个节点     
    def addNode(self, word: str) -> bool:
        if word not in self.wordIDDic:
            self.wordIDDic[word] = self.nodeCount
            self.nodeCount += 1
            return True
            
        return False
    
    def addEdges(self, firstWord :str, secondWord: str):
        firstID = self.wordIDDic[firstWord]
        secondID = self.wordIDDic[secondWord]
        self.edges[firstID].append(secondID)
        self.edges[secondID].append(firstID)
        return
    
    # 添加一个词的节点，和它对应的虚拟节点以及边
    def addWord(self, word):
        if self.addNode(word) == False:
            # 节点已经添加过，就不需要重复添加了
            return 
        
        # 给每个word节点添加响应的虚拟节点
        chars = list(word)
        for i in range(len(chars)):
            temp = chars[i]
            chars[i] = '*'
            virtualNode = "".join(chars)
            self.addNode(virtualNode)           #虚拟结点可能已经存在了，但是没关系，边是要加的
            self.addEdges(word, virtualNode)
            
            chars[i] = temp
        return
    
    
# solution = Solution()                  
# result = solution.ladderLength("hot", "dog", ["hot","hog","dog"])     
# print(solution.edges)
# print(result)        
        
# @lc code=end

