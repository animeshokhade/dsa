// question --> https://leetcode.com/problems/binary-tree-inorder-traversal/

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
var inorderTraversal = function(root) {
    if (!root) {
        return [];
    }
    const ans = [];
    const stack = [];
    while (root || stack.length) {
        if (root) {
            stack.push(root); 
            root = root.left; 
        } else {
            root = stack.pop();
            ans.push(root.val); 
            root = root.right;
        } 
    }
    return ans; 
};

// TC: O(N); SC: O(N)

// end 