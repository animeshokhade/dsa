// question --> https://leetcode.com/problems/single-number/

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let ans = 0;
    for (let index = 0; index < nums.length; index++) {
        ans ^= nums[index];
    }
    return ans
};

// TC: O(N); SC: O(1)
// end