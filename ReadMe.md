
## [46] 全排列
1. 全排列的终止条件： 只剩一个元素为加入排列
2. n和n-1的关系。 遍历n，取出每个元素，加上剩余的所有排列组合的可能。
3. 有大量的数组删除和拷贝操作，可能可以优化。

## [105] 从前序与中序遍历序列构造二叉树
1. 递归算法，找到规模N和N-1的关系，这边是难点。
2. 通过前序遍历找到跟结点，中序遍历找左右结点，这里递归的条件找中序结点的下标需要用到上一次的结果，所以用Swift 嵌套函数捕获preorderIndex变量，不使用成员变量。
3. 算法想清楚了，不代表代码就能写对。犯了两个错误，map应该存的是inorder的下标，而不是preorder的下标。 preorderIndex 索引在获取子树的根节点索引之后，划分左右子树之前 + 1. 详见代码。 
4. 在写下代码的那一刻就要保证正确，而不是写完，提交，遇到错误再修改。这样对、编写代码的能力是上不去的。

## [106] 从中序与后序遍历序列构造二叉树
1. 原理和[105]类似，但是下标索引还是超出两次
2. 注意左右边界，右边界指向数组最后一个元素的下一个位置。也就是array.cout
3. 和[105]不同的是，这里应该先构建右子树。感觉做了两道题，把可能犯错的地方都犯了。


## [144] 二叉树的前序遍历
1. 递归调用版本挺容易实现的， 代码也很简洁。 12ms，29.45%
2. 使用栈迭代的方式实现确实比较快一些，用了8ms， 77.3%。
3. 还是要注意入栈的顺序，right先入栈。

## [145] 二叉树的后序遍历
1. 注意标识已经访问的对象就可以了。
这个难度竟然是困难的， 而 590是简单的。

### [236] 二叉树的最近公共祖先
1. 使用递归方式实现  8m
深度优先搜索，如果一个节点和它的左右子树找到了两个节点， 则找到公共祖先节点
由于是深度优先搜索，所以是最近的公共祖先节点
递归思想很好用，甚至可以不需要关心具体的实现细节，只要步骤上没错就能得到答案。
运行速度也比较快，会消耗内存

2. 非递归版本，找到p，q的父节点，再比较。  21ms， 看似操作变少了，反而更慢。

## [589] N叉树的前序遍历
从590拷贝代码过来，把函数名也拷贝过来了。
拷贝代码是个很容易出错的行为，要留心。

## [590] N叉树的后序遍历
迭代方式求解注意两点
1. children元素入栈的顺序从右向左
2. 判断是否pop的条件还要判断这个元素是否已经访问过，这样才不会产生死循环
