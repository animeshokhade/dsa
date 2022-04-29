// question --> https://leetcode.com/problems/first-missing-positive/

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    let i = 1; 
    let ans = false; 
    let set = new Set(nums); 
    while (!ans) {
        if (set.has(i)) {
            i += 1; 
            continue; 
        }
        ans = i; 
    }
    return ans; 
};

// TC: O(N); SC: O(N)

// Alternative Approach

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    for (let index = 0; index < nums.length; index++) {
        while ((nums[index] >= 1) && (nums[index] <= nums.length) && (nums[index] != index + 1) && (nums[index] != nums[nums[index] - 1])) {
            let temp = nums[nums[index] - 1]; 
            nums[nums[index] - 1] = nums[index]; 
            nums[index] = temp; 
        }
    }
    for (let index = 0; index < nums.length; index++) {
        if (nums[index] !== index + 1) {
            return index + 1; 
        }
    }
    return nums.length + 1; 
};

// TC: O(N); SC: O(1)

// end 