/*
 * @lc app=leetcode.cn id=127 lang=swift
 *
 * [127] 单词接龙
 */

// @lc code=start
let NotFound = -1

public struct Queue<T> {
  fileprivate var array = [T?]()
  fileprivate var head = 0

  public var isEmpty: Bool {
    return count == 0
  }

  public var count: Int {
    return array.count - head
  }

  public mutating func enqueue(_ element: T) {
    array.append(element)
  }

  public mutating func dequeue() -> T? {
    guard let element = array[guarded: head] else { return nil }

    array[head] = nil
    head += 1

    let percentage = Double(head)/Double(array.count)
    if array.count > 50 && percentage > 0.25 {
      array.removeFirst(head)
      head = 0
    }

    return element
  }

  public var front: T? {
    if isEmpty {
      return nil
    } else {
      return array[head]
    }
  }
}

extension Array {
    subscript(guarded idx: Int) -> Element? {
        guard (startIndex..<endIndex).contains(idx) else {
            return nil
        }
        return self[idx]
    }
}

struct Node{
    let word: String
    let level: Int
}

class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        var queue = Queue<Node>()
        var remainWordList = wordList
        queue.enqueue(Node.init(word: beginWord, level: 1))
        while let node = queue.dequeue() {
            if node.word == endWord {
                return node.level
            }
            
            let newBeginWords = extractOneCharDifferentWords(beginWorkd: node.word, wordList: remainWordList)
            for newBegin in newBeginWords {
                queue.enqueue(Node.init(word: newBegin, level: node.level + 1))
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
        
        return differrentCount == 1
    }
}
// @lc code=end

