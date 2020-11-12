#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start


# 使用front，last 都用来表示当前可以插入的位置，
# front初始值为0，last初始值为1 （这个是关键）
# 如果获取值，front += 1， last -= 1
# 使用count字段来存储当前的元素个数，这样不需要浪费数组一个元素的空间来区分满和空的状态
# 在取模的下标计算上比较方便
# 浪费一个数组的空间来区别空和满的状态 

class MyCircularDeque:
    size = 0
    storage = None
    front = 0
    last = 1
    count = 0
    
    def __init__(self, k: int):
        assert k > 0 
        self.size = k
        self.storage = [None] * self.size
          

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.storage[self.front] = value
        self.front = (self.front - 1) % self.size
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
       if self.isFull():
           return False
       self.storage[self.last] = value
       self.last = (self.last + 1) % self.size
       self.count += 1
       return True 

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        # self.storage[self.front]
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.last = (self.last -1 + self.size) % self.size
        self.count -= 1
        # self.storage[self.last]
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.storage[(self.front + 1 + self.size) % self.size]   

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.storage[(self.last - 1 + self.size) % self.size]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        if self.count == self.size:
            return True
        else: 
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

