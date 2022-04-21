// question --> https://leetcode.com/problems/spiral-matrix-ii/

/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    let ans = new Array();
    for (let i = 0; i < n; i++) {
        ans[i] = new Array(n);
        for (let j = 0; j < n; j++) {
            ans[i][j] = 0;
        }
    }
    let r = 0; 
    let c = 0; 
    let s = 1; 
    let dirc = 1; 
    
    while (s <= n * n) {
        ans[r][c] = s; 
        s += 1; 
        if (dirc == 1) {
            c += 1; 
            if ((c == n) || (ans[r][c] != 0)) {
                dirc = 2; 
                c -= 1; 
                r += 1; 
            }
        }
        else if (dirc == 2) {
            r += 1; 
            if ((r == n) || (ans[r][c] != 0)) {
                dirc = 3; 
                r -= 1; 
                c -= 1; 
            }
        }
        else if (dirc == 3) {
            c -= 1; 
            if ((c < 0) || (ans[r][c] != 0)) {
                dirc = 4; 
                c += 1; 
                r -= 1; 
            }
        }
        else if (dirc == 4) {
            r -= 1; 
            if ((r < 0) || (ans[r][c] != 0)) {
                dirc = 1; 
                r += 1; 
                c += 1; 
            }
        }
    }
    return ans;
};

// TC: O(N^2); SC: O(N^2)

// end 