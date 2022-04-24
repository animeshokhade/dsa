// question --> https://leetcode.com/problems/k-th-symbol-in-grammar/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthGrammar = function(n, k) {
    // Base condition
    
    if (n == 1) {
        return 0; 
    }
    
    // Recursion relation 
    
    let mid = 1 << (n - 2); 
    if (k <= mid) {
        return kthGrammar(n - 1, k); 
    } else {
        return 1 - kthGrammar(n - 1, k - mid); 
    }
};

// TC: O(N); SC: O(N)

// end 