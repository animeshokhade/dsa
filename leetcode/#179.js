// question --> https://leetcode.com/problems/largest-number/

/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    const ans = nums.map(String).sort((a, b) => a.concat(b) >= b.concat(a) ? -1 : 1).join('');
    return ans.charAt(0) === '0' ? '0' : ans; 
};

// TC: O(NlogN); SC: O(N)

// end 