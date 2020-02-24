/*
 * @lc app=leetcode.cn id=236 lang=java
 *
 * [236] 二叉树的最近公共祖先
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Stack<TreeNode> stack = Stack<>()
        Map<TreeNode, TreeNode> parentMap = new HashMap<>()

        parentMap.put(root, null)
        stack.push(root)
        while(parentMap.contains(p) == false || parentMap.contains(q) == false){
            TreeNode node = stack.pop()
            if(node.right != null){
                stack.push(node.right);
                parentMap[node.right] = node
            }
            if(node.left != null){
                stack.push(node.left);
                parentMap[node.left] = node;
            }
        }
        
        Set<TreeNode> ancestors = new HasSet<>();
        while(p != null){
            ancestors.add(p);
            p = parentMap[p];
        }

        while(ancestors.contains(q) == false){
            q = parentMap[q];
        }
        return q;
    }
}

// //深度优先搜索，如果一个节点和它的左右子树找到了两个节点， 则找到公共祖先节点
// //由于是深度优先搜索，所以是最近的公共祖先节点
// //递归思想很好用，甚至可以不需要关心具体的实现细节，只要步骤上没错就能得到答案。
// //运行速度也比较快，会消耗内存
// class Solution {
//     private TreeNode lcaNode = null;
//     private int recurseTree(TreeNode currentNode, TreeNode p, TreeNode q){
//         if(currentNode == null){
//             return 0;
//         }

//         //has founded 
//         if(lcaNode != null){
//              return 0;
//         }

//         int leftCount = this.recurseTree(currentNode.left, p, q);
//         int rightCount = this.recurseTree(currentNode.right, p, q);
//         int count = (currentNode == p || currentNode == q) ? 1 : 0;
//         if (leftCount + rightCount + count >= 2){
//             lcaNode = currentNode;
//         }

//         return (leftCount + rightCount + count) > 0 ? 1 : 0;
//     }
//     public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
//         this.recurseTree(root, p, q);
//         return lcaNode;
//     }
// }
// @lc code=end

