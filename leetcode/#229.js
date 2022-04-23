// question --> https://leetcode.com/problems/majority-element-ii/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    let n = nums.length; 
    let ans = new Array(); 
    let frequencyTracker = new Map(); 
    
    for (let index = 0; index < nums.length; index++) {
        if (frequencyTracker.has(nums[index])) {
            frequencyTracker.set(nums[index], frequencyTracker.get(nums[index]) + 1);
        } else {
            frequencyTracker.set(nums[index], 1);
        }
    }
    
    for (let k of frequencyTracker.keys()) {
        if (frequencyTracker.get(k) > Math.floor(n / 3)) {
            ans.push(k);
            } 
    } 
    return ans;
};

// TC: O(N); SC: O(N)

// Optimised Approach --> Boyer Moore Voting Algorithm

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    let firstMajority = 0; 
    let secondMajority = 0; 
    let firstCount = 0; 
    let secondCount = 0; 
    
    for (let index = 0; index < nums.length; index++) {
        if (nums[index] == firstMajority) {
            firstCount += 1; 
        } else if (nums[index] == secondMajority) {
            secondCount += 1; 
        } else if (firstCount == 0) {
            firstMajority = nums[index];
            firstCount = 1;
        } else if (secondCount == 0) {
            secondMajority = nums[index];
            secondCount = 1; 
        } else {
            firstCount -= 1; 
            secondCount -= 1;
        }
    }
    
    let ans = new Array(); 
    let test = Math.floor(nums.length / 3); 
    
    let tracker1 = 0; 
    let tracker2 = 0; 
    
    for (let index = 0; index < nums.length; index++) {
        if (nums[index] == firstMajority) {
            tracker1 += 1; 
        } else if (nums[index] == secondMajority) {
            tracker2 += 1; 
        }
    }
    
    if (tracker1 > test) {
        ans.push(firstMajority);
    }
    
    if (tracker2 > test) {
        ans.push(secondMajority);
    }
    
    return ans;
};

// TC: O(N); SC: O(1)

// end 
