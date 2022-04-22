// question --> https://leetcode.com/problems/single-number-iii/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    let lookup = new Set();
    
    for (let index = 0; index < nums.length; index++) {
        if (lookup.has(nums[index])) {
            lookup.delete(nums[index]); 
        }
        else {
            lookup.add(nums[index]); 
        }
    }
    
    lookup = Array.from(lookup);
    return lookup.sort(); 
};

// TC: O(N); SC: O(N)

// Optimised Approach - 01

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    let xor = 0; 
    for (let index = 0; index < nums.length; index++) {
        xor ^= nums[index];
    } 
    let firstSetBit = 0; 
    for (firstSetBit; firstSetBit < 32; firstSetBit++) {
        if ((1 << firstSetBit) & xor) {
            break; 
        }
    }
    let num1 = 0; 
    for (let index = 0; index < nums.length; index++) {
        if ((1 << firstSetBit) & nums[index]) {
            num1 ^= nums[index]; 
        }
    }
    let ans = [Math.min(num1, num1^xor), Math.max(num1, num1^xor)];
    return ans
};

// TC: O(N); SC: O(1)

// Optimal Approach - 02

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    let xor = 0; 
    for (let index = 0; index < nums.length; index++) {
        xor ^= nums[index];
    } 
    let firstSetBit = (xor & (xor - 1)) ^ xor;
    let num1 = 0; 
    for (let index = 0; index < nums.length; index++) {
        if (firstSetBit & nums[index]) {
            num1 ^= nums[index]; 
        }
    }
    let ans = [Math.min(num1, num1^xor), Math.max(num1, num1^xor)];
    return ans
};

// TC: O(N); SC: O(1)

// end 

