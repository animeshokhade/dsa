// question --> https://leetcode.com/problems/trapping-rain-water/

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    // leftMax
    
    let leftMax = new Array(); 
    let tempLeft = Number.NEGATIVE_INFINITY; 
    for (let i = 0; i < height.length; i++) {
        if (height[i] > tempLeft) {
            tempLeft = height[i]; 
        }
        leftMax.push(tempLeft); 
    }
    
    // rightMax
    
    let rightMax = new Array(); 
    let tempRight = Number.NEGATIVE_INFINITY; 
    for (let j = height.length - 1; j >= 0; j--) {
        if (height[j] > tempRight) {
            tempRight = height[j]; 
        }
        rightMax.push(tempRight); 
    }
    rightMax.reverse(); 
    
    let ans = 0; 
    if (height) {
        for (let x = 1; x < height.length; x++) {
            let water = Math.min(leftMax[x], rightMax[x]) - height[x]; 
            if (water > 0) {
                ans += water; 
            }
        }
    }
    return ans; 
};

// TC: O(N); SC: O(N)

// Alternative Approach

/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let n = height.length; 
    let left = 0; 
    let right = height.length - 1; 
    
    let ans = 0; 
    let maxLeft = Number.NEGATIVE_INFINITY; 
    let maxRight = Number.NEGATIVE_INFINITY; 
    
    while (left <= right) {
        if (height[left] <= height[right]) {
            if (height[left] >= maxLeft) {
                maxLeft = height[left]; 
            } else {
                ans += maxLeft - height[left]; 
            }
            left += 1; 
        } else {
            if (height[right] >= maxRight) {
                maxRight = height[right];
            } else {
                ans += maxRight - height[right]; 
            }
            right -= 1; 
        }
    }
    return ans; 
};

// TC: O(N); SC: O(N)

// end 