/*
 * @lc app=leetcode.cn id=127 lang=swift
 *
 * [127] 单词接龙
 */

// @lc code=start
struct Node{
    let word: String
    let level: Int
}

class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        var queue = [Node]()
        var remainWordList = wordList
        queue.append(Node.init(word: beginWord, level: 1))
        while let node = queue.first {
            queue.remove(at: 0)
            if node.word == endWord {
                return node.level
            }
            
            let newBeginWords = extractOneCharDifferentWords(beginWorkd: node.word, wordList: remainWordList)
            for newBegin in newBeginWords {
                queue.append(Node.init(word: newBegin, level: node.level + 1))
            }
            
            remainWordList.removeAll { string -> Bool in
                newBeginWords.contains(string)
            }
        }
        
        return 0
    }
    
    
    func extractOneCharDifferentWords(beginWorkd: String, wordList: [String]) -> [String]{
        var result = [String]()
        for word in wordList {
            if isOneCharDifferent(first: beginWorkd, second: word){
                result.append(word)
            }
        }
        return result
    }
    
    func isOneCharDifferent(first: String, second: String) -> Bool{
        guard first.count == second.count else {
            return false
        }
        
        var differrentCount = 0
        for i in first.indices {
            if first[i] != second[i] {
                differrentCount += 1
                if differrentCount > 1 {
                    return false
                }
            }
        }
        
        return differrentCount <= 1
    }
}
// @lc code=end

