// question --> https://leetcode.com/problems/missing-number/

/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let sumNaturalNumbers = Math.floor((nums.length * (nums.length + 1)) / 2);
    let sum = 0; 
    for (let index = 0; index < nums.length; index++) {
        sum += nums[index];
    }
    return sumNaturalNumbers - sum;
};

// TC: O(N); SC: O(1)

// end 