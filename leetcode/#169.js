// question --> https://leetcode.com/problems/majority-element/

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let majority = nums[0];
    let count = 1; 
    
    for (let index = 1; index < nums.length; index++) {
        if (majority == nums[index]) {
            count += 1; 
        } else {
            count -= 1;
            if (count == 0) {
                majority = nums[index];
                count = 1;
            }
        }
    }
    
    return majority;
};

// TC: O(N); SC: O(1)

// end 