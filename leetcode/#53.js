// question --> https://leetcode.com/problems/maximum-subarray/

var maxSubArray = function(nums) {
    let maxSoFar = nums[0];
    let maxEndingHere = nums[0];
    for (let index = 1; index < nums.length; index++) {
        let temp = maxEndingHere + nums[index];
        maxEndingHere = Math.max(temp, nums[index]);
        maxSoFar = Math.max(maxSoFar, maxEndingHere);
    }
    return maxSoFar
};

// TC: O(N); SC: O(1)

// Alternative Approach

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let summ = 0; 
    let ans = nums.reduce(function(a, b) {
        return Math.max(a, b);
    })
    if (ans < 0) {
        return ans; 
    } else {
        ans = 0; 
    }
    
    for (let i = 0; i < nums.length; i++) {
        summ += nums[i]; 
        if (summ < 0) {
            summ = 0; 
        }
        ans = Math.max(ans, summ) 
    }
    return ans; 
};

// end