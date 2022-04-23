// question --> https://leetcode.com/problems/sort-colors/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let start = 0; 
    let mid = 0; 
    let end = nums.length - 1; 
    
    while (mid <= end) {
        if (nums[mid] === 1) {
            mid += 1;
        } else if (nums[mid] === 0) {
            [nums[start], nums[mid]] = [nums[mid], nums[start]];
            start += 1; 
            mid += 1; 
        } else if (nums[mid] == 2) {
            [nums[mid], nums[end]] = [nums[end], nums[mid]]; 
            end -= 1; 
        }
    }
    return nums; 
};

// TC: O(N); SC: O(N)

// end 