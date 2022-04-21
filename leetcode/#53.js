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

// end