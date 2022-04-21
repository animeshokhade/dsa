// question --> https://leetcode.com/problems/number-of-1-bits/

/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let setBit = 0; 
    while (n) {
        n = n & (n - 1);
        setBit += 1;
    }
    return setBit; 
};

// TC: O(logN); SC: O(1)

// end