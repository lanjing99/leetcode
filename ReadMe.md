## [20] 有效的括号匹配

1. 使用栈来实现括号匹配。Python中没看到Stack数据结构，使用List来替代。
2. 增加一个dic来存储括号的对应关系，可以简化代码，增加灵活性。
3. 判断key也从字段中获取数据，进一步简化代码
4. 栈预存一个？能够简化栈是否为空的判断，提高执行效率。速度快过70%变成速度快过94%

## [24] 两两交换链表中的节点

用递归很好理解，代码也简单，递归是个强大的工具。

## [46] 全排列
1. 全排列的终止条件： 只剩一个元素为加入排列
2. n和n-1的关系。 遍历n，取出每个元素，加上剩余的所有排列组合的可能。
3. 有大量的数组删除和拷贝操作，可能可以优化。

## [47] 全排列 II
1 在[46]的全排列的基础上，利用Set去重。可以实现，不是个好策略。用时528ms，击败10.53%
2 在排列之前提前剪枝，极大提高了效率， 48ms， 94.74%

## [64] 最小路径和
1. 主要算法理解起来简单，但是细节的地方错了两次，用了半个小时的时间调试。
2. 初始化results的时候，计算column出错。results的作用一开始没想明白。

## [77] 组合
1. 弄清楚 N 和 N-1 之间的关系，这里要求的组合是不重复的。返回条件是k==1的时候
2. 注意小标， startIndex从1开始，而不是从0， 判断条件是tartIndex <= n - count + 1， 用特殊值试一下。例如4 2

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

## [105] 从前序与中序遍历序列构造二叉树
1. 递归算法，找到规模N和N-1的关系，这边是难点。
2. 通过前序遍历找到跟结点，中序遍历找左右结点，这里递归的条件找中序结点的下标需要用到上一次的结果，所以用Swift 嵌套函数捕获preorderIndex变量，不使用成员变量。
3. 算法想清楚了，不代表代码就能写对。犯了两个错误，map应该存的是inorder的下标，而不是preorder的下标。 preorderIndex 索引在获取子树的根节点索引之后，划分左右子树之前 + 1. 详见代码。 
4. 在写下代码的那一刻就要保证正确，而不是写完，提交，遇到错误再修改。这样对、编写代码的能力是上不去的。

## [106] 从中序与后序遍历序列构造二叉树
1. 原理和[105]类似，但是下标索引还是超出两次
2. 注意左右边界，右边界指向数组最后一个元素的下一个位置。也就是array.cout
3. 和[105]不同的是，这里应该先构建右子树。感觉做了两道题，把可能犯错的地方都犯了。

## [107] 二叉树的层次遍历 II
1. Swift Array 是个值类型，有时候也挺麻烦的，要先取出数组，修改，然后再复制改回去
2. level信息当做参数来传递

## [122] 买卖股票的最佳时机 II
1. 每天把能挣到的钱都挣了，总共的利润就是最大的。这可不就是贪心吗？：D
2. 能用贪心算法的话，就会发现贪心算法往往是最简单也是最优的，难的地方在于怎么发现是可以贪心的，怎么贪心。

## [127] 单词接龙
1. 在一个for循环里递归调用，是深度优先遍历，并不是广度优先。（广度优先遍历是要用队列来实现，用递归是实现不了的。）也就是循环加栈并不是一个队列。
2. 二叉树中的层次遍历和先序遍历是不同的。

## [144] 二叉树的前序遍历
1. 递归调用版本挺容易实现的， 代码也很简洁。 12ms，29.45%
2. 使用栈迭代的方式实现确实比较快一些，用了8ms， 77.3%。
3. 还是要注意入栈的顺序，right先入栈。

## [145] 二叉树的后序遍历
1. 注意标识已经访问的对象就可以了。
这个难度竟然是困难的， 而 590是简单的。

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
深度优先搜索，如果一个节点和它的左右子树找到了两个节点， 则找到公共祖先节点
由于是深度优先搜索，所以是最近的公共祖先节点
递归思想很好用，甚至可以不需要关心具体的实现细节，只要步骤上没错就能得到答案。
运行速度也比较快，会消耗内存

2. 非递归版本，找到p，q的父节点，再比较。  21ms， 看似操作变少了，反而更慢。

## [455] 分发饼干
1. 为了简化问题，胃口大小和饼干尺寸使用前需要排序一下

## [589] N叉树的前序遍历
从590拷贝代码过来，把函数名也拷贝过来了。
拷贝代码是个很容易出错的行为，要留心。

## [590] N叉树的后序遍历
迭代方式求解注意两点
1. children元素入栈的顺序从右向左
2. 判断是否pop的条件还要判断这个元素是否已经访问过，这样才不会产生死循环

## [860] 柠檬水找零
1. 认真读懂题目，才发现原来很简单。
2. 原来还想着用一个字典来存放5美元和10美元的计数，一个简单变量就行了，看来是牛刀用习惯了，忘记简单方法了。