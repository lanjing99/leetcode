[toc]

## [20] 有效的括号匹配

1. 使用栈来实现括号匹配。Python中没看到Stack数据结构，使用List来替代。
2. 增加一个dic来存储括号的对应关系，可以简化代码，增加灵活性。
3. 判断key也从字段中获取数据，进一步简化代码
4. 栈预存一个？能够简化栈是否为空的判断，提高执行效率。速度快过70%变成速度快过94%

## [22] 括号生成

使用递归方式完成，关键是如何将问题拆解成更简单的子问题，这个估计要多做题才能解决。

## [24] 两两交换链表中的节点

用递归很好理解，代码也简单，递归是个强大的工具。

## [42] 接雨水
1. 暴力解法，找每个位置可以存放的水是多少。找到左右边界。在此基础上存储每个位置的左右边界最大值能将时间复杂度从O(n^2)编程O(n).
2. 使用栈解法
   1. 单调递减的栈很好用。
   2. 弄清楚做边界和右边界与面积的关系
3. 使用双向指针法：根据暴力解法，使用双指针来求解。假设右边有一堵很高的强。左边要怎样才能存水？要看左边边界的高度和当前位置的高度。当前位置比较矮，就能存水，否则当前位置会变成左边新的墙。

## [46] 全排列
1. 全排列的终止条件： 只剩一个元素为加入排列
2. n和n-1的关系。 遍历n，取出每个元素，加上剩余的所有排列组合的可能。
3. 有大量的数组删除和拷贝操作，可能可以优化。
4. 感觉递归操作效率不低，但是Python数组复制怎么没影响效率，有点奇怪。

## [47] 全排列 II
1. 在[46]的全排列的基础上，利用Set去重。可以实现，不是个好策略。用时528ms，击败10.53%
2. 在排列之前提前剪枝，极大提高了效率， 48ms， 94.74%
3. 在源头消除重复，而不是用set去重





## [49] 字母异位词分组

先对字符串排序，再放到字典里比较。

要注意的是，Python字典的使用跟 其它语言不一样，字典获取不存在的value会抛出错误。

存到字典里的值也是一个引用类型的值，不是值类型的

## [64] 最小路径和
1. 主要算法理解起来简单，但是细节的地方错了两次，用了半个小时的时间调试。
2. 初始化results的时候，计算column出错。results的作用一开始没想明白。

## [77] 组合
这个解法现在没搞懂。。

1. 弄清楚 N 和 N-1 之间的关系，这里要求的组合是不重复的。返回条件是k==1的时候
2. 注意小标， startIndex从1开始，而不是从0， 判断条件是tartIndex <= n - count + 1， 用特殊值试一下。例如4 2



2. 使用递归解法，如何将问题N分解成N-1。这个组合规模N可以分解为
   1. 取第一个数，从剩下的去k-1个数
   2. 不取第一个数，从生下的取k个数。

## [84] 柱状图中最大的矩形

1. 使用遍历高度的解法，算法复杂度O(n^2)，最后两个用例超时了。要注意查找左边和右边高度的边界情况。

2. 使用栈的方式来解决

   1. 思考一下左边界和右边界，分别是比当前值小的时候。

   2. 维护一个有序栈，当前值比栈顶值大的时候，入栈。当前值比栈顶值小，说明栈顶值的右边界已经到了，左边界是上一个元素。这样就能计算矩形的宽度了。

   3. 当栈不为空（多于一个元素）的时候，要继续处理。

   4. 注意[0],[1], 这种边界情况的处理。

      

## [91] 解码方法
1. 用递归，0的判断条件不好实现。从后往前推推不下去。
2. 0的判断有点麻烦，这个题目需要重新看。边界条件比较麻烦。



## [94] 二叉树的中序遍历

1. 使用递归方法实现 （确实比较简单）

   - Your runtime beats 43.47 % of python3 submissions
   - Your memory usage beats 9.32 % of python3 submissions (13.5 MB)

2. 使用栈迭代方法

   - Your runtime beats 87.43 % of python3 submissions
   - Your memory usage beats 88.27 % of python3 submissions (13.3 MB)

   python列表为空时，返回false，这是个语法糖的功能，不太严谨。

   ```python
   while p or stack:
               while p:
                   stack.append(p)
                   p = p.left
               top = stack.pop()
               result.append(top.val)
               p = top.right
   ```

## [98] 验证二叉搜索树

1. 递归实现比较容易，关键是将一个节点的最小值和最大值想清楚。画一个树出来，然后用纸和笔推演几步。
2. 传3个参数就够了，当前结点，当前节点的最小值和最大值。父节点不需要传。



非递归实现，带状态

1. 遍历的结构和前序遍历一致
2. 要注意的是min和max的额外状态每一层都不同，要入栈。进入下一级的时候，如何更新min和max



## [105] 从前序与中序遍历序列构造二叉树
1. 递归算法，找到规模N和N-1的关系。确定根节点，列出左子树和右子树，递归实现比较容易。
2. 考虑输入为空数组的边界情况，这个一直没做。
3. 通过前序遍历找到跟结点，中序遍历找左右结点，这里递归的条件找中序结点的下标需要用到上一次的结果，所以用Swift 嵌套函数捕获preorderIndex变量，不使用成员变量。
4. 算法想清楚了，不代表代码就能写对。犯了两个错误，map应该存的是inorder的下标，而不是preorder的下标。 preorderIndex 索引在获取子树的根节点索引之后，划分左右子树之前 + 1. 详见代码。 
5. **在写下代码的那一刻就要保证正确，而不是写完，提交，遇到错误再修改**。这样对、编写代码的能力是上不去的。

## [106] 从中序与后序遍历序列构造二叉树
1. 解法1：使用递归，先利用后续找到root，再根据中序区分左子树和右子树。
2. 解法2：使用迭代。
   1. 原理和[105]类似，但是下标索引还是超出两次
   2. 注意左右边界，右边界指向数组最后一个元素的下一个位置。也就是array.cout
   3. 和[105]不同的是，这里应该先构建右子树。感觉做了两道题，把可能犯错的地方都犯了。

## [107] 二叉树的层次遍历 II
1. Swift Array 是个值类型，有时候也挺麻烦的，要先取出数组，修改，然后再复制改回去 (可以用inout参数啊)
2. level信息当做参数来传递

## [122] 买卖股票的最佳时机 II
1. 每天把能挣到的钱都挣了，总共的利润就是最大的。这可不就是贪心吗？：D
2. 能用贪心算法的话，就会发现贪心算法往往是最简单也是最优的，难的地方在于怎么发现是可以贪心的，怎么贪心。

## [127] 单词接龙
1. 在一个for循环里递归调用，是深度优先遍历，并不是广度优先。（广度优先遍历是要用队列来实现，用递归是实现不了的。）也就是循环加栈并不是一个队列。
2. 二叉树中的层次遍历和先序遍历是不同的。

## [144] 二叉树的前序遍历
1. 解法1：递归调用版本挺容易实现的， 代码也很简洁。 12ms，29.45%

2. 解法2：使用栈迭代的方式实现确实比较快一些，用了8ms， 77.3%。

   1. 前序遍历用栈实现也很方便，注意当前指针和stack为空的判断是或条件。代码条件比较精巧。

   ```Python
    while p is not None or len(stack) != 0:
               while p is not None:
                   result.append(p.val)
                   stack.append(p)
                   p = p.left
                   
               top = stack.pop()    
               p = top.right
   ```

   

## [145] 二叉树的后序遍历
1. 这里要注意的是，根节点要最后出栈。所以要先遍历左子树，当左子树为空时，要判断右子树是否已经访问过。所以和前序、中序遍历相比，需要一个额外的变量指示上次访问过的节点。

关于用栈迭代二叉树做个总结：三个遍历的共同点，都是先左子树、在右子树，只是在不同实际访问根节点。

1. 前序遍历：在入栈的时候即可访问当前跟节点。
2. 中序遍历：在节点出栈的时候访问跟节点
3. 后续遍历：访问左右子树后，根节点才能出栈，在出栈的时候访问节点。需要一个变量指向上次访问的节点。

递归确实是个好工具，能简化问题.

## [155] 最小栈

1. 用栈来存储局部最小值
2. 因为出栈的时候最小值要出栈，所以当等于当前最小值的时候，也要入栈。

## [206] 翻转链表
链表为空的时候要判断，一定要考虑程序的健壮性

递归版本： 关键点在于下面两句的理解，看来递归的样式很多，写出来的代码很简单，过程却有点难以理解
head.next.next = head
head.next = None

``
def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
            
        result = self.reverseList(head= head.next)
        head.next.next = head
        head.next = None
    
        return result
``

## [236] 二叉树的最近公共祖先
1. 使用递归方式实现  8m
   第一种解法
      深度优先搜索(后序遍历，先判断子节点，再判断根节点。
      如果一个节点和它的左右子树找到了两个节点， 则找到公共祖先节点
      如果在左右子树中找到一个，当前根节点满足条件，那么当前节点就是最小公共祖先节点。
   第二种解法
      原理跟上面类似，但是建立在一定有公共父节点的基础上，只要节点在树立，这个逻辑是成立的。
      p，q的公共父节点不是在root的左子树，就是在右子树，或者是root节点。参考这个[题解](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/)
      ```
      if root is None or root == p or root == q:
            return root
      ```

由于是深度优先搜索，所以是最近的公共祖先节点
递归思想很好用，甚至可以不需要关心具体的实现细节，只要步骤上没错就能得到答案。
运行速度也比较快，会消耗内存。

1. 非递归版本，找到p，q的父节点，再比较。  21ms， 看似操作变少了，反而更慢。

## [239] 滑动窗口最大值
1. 用双向队列来求解局部最大值。
2. 将数组的下标存入队列，而不是值，因为根据下标可以计算当前窗口大小。
3. 代码根据leetcode返回错误的数据进行调试，能求得正确结果，但是提交leetcode代码时却跑不通。有点诡异。

## [429] N叉树的层序遍历
使用队列来做层次遍历，要注意的是
1. 如何开始下一层次，每一层次出队列的次数为某一层次入队列后的长度就可以了。
2. deque 判断长度，直接 while q: 就可以判断是否为空，这个语法有点诡异啊，是否是语法糖。

## [455] 分发饼干
1. 为了简化问题，胃口大小和饼干尺寸使用前需要排序一下

## [589] N叉树的前序遍历
从590拷贝代码过来，把函数名也拷贝过来了。
拷贝代码是个很容易出错的行为，要留心。

## [590] N叉树的后序遍历
迭代方式求解注意两点
1. children元素入栈的顺序从右向左
2. 判断是否pop的条件还要判断这个元素是否已经访问过，这样才不会产生死循环

## [641] 设计循环双端队列
使用front，last 都用来表示当前可以插入的位置，
front初始值为0，last初始值为1 （这个是关键）
如果获取值，front += 1， last -= 1
使用count字段来存储当前的元素个数，这样不需要浪费数组一个元素的空间来区分满和空的状态
在取模的下标计算上比较方便
浪费一个数组的空间来区别空和满的状态 

## [860] 柠檬水找零
1. 认真读懂题目，才发现原来很简单。
2. 原来还想着用一个字典来存放5美元和10美元的计数，一个简单变量就行了，看来是牛刀用习惯了，忘记简单方法了。