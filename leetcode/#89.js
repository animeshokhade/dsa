// question --> https://leetcode.com/problems/gray-code/

/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    // Base condition
    
    if (n == 1) {
        return [0, 1]; 
    }
    
    // Recursive relation
    
    let firstHalf = grayCode(n - 1); 
    let secondHalf = new Array(); 
    let j = firstHalf.length - 1; 
    for (j; j >= 0; j--) {
        secondHalf.push((1 << (n - 1)) + firstHalf[j]); 
    }
    return [].concat(firstHalf, secondHalf); 
};

// TC: O(2^N); SC:O(2^N)

// Alternative Approach

/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    let ans = new Array(); 
    for (let code = 0; code < (1 << n); code++) {
        ans.push((code >> 1) ^ code); 
    }
    return ans; 
};

// TC: O(2^N); SC: O(2^N)

// end 