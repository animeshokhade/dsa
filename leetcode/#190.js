// question --> https://leetcode.com/problems/reverse-bits/

/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    let q = n; 
    let r = 0;
    let binA = '';
    
    while (q >= 1) {
        r = q % 2;
        q = Math.floor(q / 2);
        binA += r.toString(); 
    }
    
    let zeros = 32 - binA.length;
    for (let i = 0; i < zeros; i++) {
        binA += '0';
    }
    
    let x = 31; 
    let j = 0; 
    let ans = 0; 
    while (j < 32) {
        if (binA[j] == '1') {
            ans += Math.pow(2, x);
        }
        x -= 1;
        j += 1;
    }
    
    return ans;
};

// TC: O(logN); SC: O(logN)

// end