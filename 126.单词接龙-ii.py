#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    
    wordIDDic = None
    idWordDic = None
    parents = None
    nodeCount = 0
    edges = None # 是字典，下标是节点的编号，值以相邻的边的数组
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.wordIDDic = dict()
        self.nodeCount = 0
        # 这个意思是创建一个字典，value如果没有值的话，默认值是list类型的[],确实挺方便的。
        # 但是感觉Python的这些语法糖很细碎
        self.edges = defaultdict(list)  
        
        # 添加词语，构建一个word的图结构
        for word in wordList:
            self.addWord(word)
            
        
        self.addWord(beginWord)
        # 根据id获取word的内容
        self.idWordDic = {value: key for key, value in  self.wordIDDic.items()}
        
        # distance[node] 表示 node节点到beginword节点的距离
        # 要有distance[] 数据，因为图是双向，否则层级遍历的时候，会回到父节点
        distance = [float("inf")] * self.nodeCount
        self.parents = []
        for i in range(0, self.nodeCount):
            self.parents.append(set())
            
        distance[self.wordIDDic[beginWord]] = 0
        
        
        if endWord not in self.wordIDDic:
            return []
        
        wordQueue = deque([self.wordIDDic[beginWord]])
        level = 1
        while wordQueue:
            levelLength = len(wordQueue)  ## 当前层节点的个数
            while levelLength > 0:
                levelLength -= 1 
                wordID = wordQueue.popleft()
                # 返回结果
                if wordID == self.wordIDDic[endWord]:
                    # 退出两重循环
                    wordQueue = None
                    break

                for x in self.edges[wordID]:
                    
                    # 因为是层次遍历，不可能发生下一次遍历到的路径比上一次要短
                    # A->B， B->A时，就是distance[x] < level的时候，这个时候不需要处理
                    # assert distance[x] >= level
                    
                    # 这个节点没被访问过
                    if distance[x] == float('inf'):
                        distance[x] = level
                        # 添加父节点
                        self.parents[x].add(wordID)
                        wordQueue.append(x)
                    elif distance[x] == level:
                        # 另一个父节点
                        self.parents[x].add(wordID)
                        # 不需要遍历这个节点的子节点了
            level += 1
            
        
        result = []
        self.allPaths(self.wordIDDic[endWord], self.wordIDDic[beginWord], [], result)
            
        return result
    
    

    
    def allPaths(self, beginWordID: int, endWordID: int, prefix: List[str], result: List[List[str]]):
        if beginWordID == endWordID:
            prefix.append(self.idWordDic[beginWordID])
            prefix.reverse()
            result.append(prefix)
            return result
        
        for pid in self.parents[beginWordID]:
            prefixCopy = prefix.copy()
            if '*' not in self.idWordDic[beginWordID]:
                prefixCopy.append(self.idWordDic[beginWordID])
            self.allPaths(pid, endWordID, prefixCopy, result)
        return
    
     
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
result = Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(result)
# @lc code=end

