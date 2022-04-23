// question --> https://leetcode.com/problems/longest-common-prefix/

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let ans = strs.reduce((a, b) => a.length <= b.length ? a : b);
    let iterations = ans.length; 
    
    let index = 0; 
    
    for (index; index < iterations; index++) {
        let temp = ans[index];
        for (let i = 0; i < strs.length; i++) {
            if (strs[i][index] != temp) {
                if (index == 0) {
                    return ''
                }
                return ans.slice(0, index);
            } 
        }
    }
    return ans.slice(0, index + 1);
};

// TC: O(N^2); SC: O(N)

// end 