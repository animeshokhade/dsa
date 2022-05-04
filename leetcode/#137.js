// question --> https://leetcode.com/problems/single-number-ii/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var singleNumber = function(nums) {
    let dictionary = {};
    
    for (let index = 0; index < nums.length; index++) {
        if (dictionary[nums[index]] !== undefined) {
            dictionary[nums[index]] += 1; 
        } else {
            dictionary[nums[index]] = 1; 
        }
    }
    
    for (let index = 0; index < nums.length; index++) {
        if (dictionary[nums[index]] === 1) {
            return nums[index]; 
        }
    }
};

// TC: O(N); SC:O(N)

// Optimised Approach

/**
 * @param {number[]} nums
 * @return {number}
 */
 var singleNumber = function(nums) {
    let ones = 0; 
    let twos = 0; 
    let commonMask = 0; 
    
    for (let index = 0; index < nums.length; index++) {
        twos |= ones & nums[index]; 
        ones ^= nums[index]; 
        commonMask = ~(ones & twos); 
        ones &= commonMask; 
        twos &= commonMask; 
    }
    
    return ones; 
};

// TC: O(N); SC:O(1)

// end 