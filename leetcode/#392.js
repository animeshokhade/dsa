// question --> https://leetcode.com/problems/is-subsequence/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let S = 0, T = 0; 
    while (S < s.length && T < t.length) {
        if (s[S] === t[T]) {
            S += 1; 
            T += 1; 
        } else {
            T += 1; 
        }
    }
    if (S === s.length) {
        return true; 
    }
    return false; 
};

// TC: O(N); SC: O(N)

// end 