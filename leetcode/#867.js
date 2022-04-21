// question --> https://leetcode.com/problems/transpose-matrix/

/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var transpose = function(matrix) {
    let rows = matrix.length;
    let cols = matrix[0].length;
    let ans = new Array();
    for (let c = 0; c < cols; c++) {
        ans[c] = Array(rows); 
    }
    
    for (let c = 0; c < cols; c++) {
        for (let r = 0; r < rows; r++) {
            ans[c][r] = matrix[r][c];
        }
    }
    return ans;
};

// TC: O(N); SC: O(N) 

// end