// question --> https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/submissions/

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canMakeArithmeticProgression = function(arr) {
    let n = arr.length;
    arr.sort(function(a, b) {return a - b}); 
    let constDiff = arr[1] - arr[0]; 
    
    for (let index = 1; index < n; index++) {
        if (arr[index] - arr[index - 1] != constDiff) {
            return 0; 
        }
    }
    return 1;
};

// TC: O(NlogN); SC: O(1)

// end 