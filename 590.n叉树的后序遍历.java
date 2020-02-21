/*
 * @lc app=leetcode.cn id=590 lang=java
 *
 * [590] N叉树的后序遍历
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    public List<Integer> postorder(Node node) {
        List<Integer> result = new ArrayList<>();
        helper(node, result);
        return result;
    }

    private void helper(Node node, List<Integer> result){
        if(node == null){
            return;
        }

        for(Node n: node.children){
            helper(n, result);
        }
        result.add(node.val);
    }
}
// @lc code=end

