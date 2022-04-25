// question --> https://leetcode.com/problems/binary-tree-postorder-traversal/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var postorderTraversal = function(root) {
    if (!root) {
        return [];
    }
    const stack = [];
    const processor = [];
    const ans = [];
    stack.push(root); 
    while (stack.length) {
        let node = stack.pop(); 
        processor.push(node); 
        if (node.left) {
            stack.push(node.left);
        }
        if (node.right) {
            stack.push(node.right); 
        }
    }
    while (processor.length) {
        let node = processor.pop(); 
        ans.push(node.val); 
    }
    return ans; 
};

// TC: O(N); SC: O(N)

// end 