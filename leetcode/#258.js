// question --> https://leetcode.com/problems/add-digits/submissions/

/**
 * @param {number} num
 * @return {number}
 */
var summ = function(num) {
  if (Math.floor(num / 10) == 0) {
      return num % 10; 
  } else {
      return summ(Math.floor(num / 10)) + num % 10; 
  }
};

var addDigits = function(num) {
    ans = summ(num); 
    if (ans > 9) {
        return addDigits(ans); 
    } else {
        return ans; 
    }
};

// TC: O(logN - base10); SC: O(logN - base10)

// Optimised Approach

/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    if (num % 9 != 0) {
        return num % 9; 
    } else if (num == 0) {
        return 0; 
    } else {
        return 9; 
    }
};

// TC: O(1); SC: O(1)

// end 
