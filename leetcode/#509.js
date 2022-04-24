// question --> https://leetcode.com/problems/fibonacci-number/

/**
 * @param {number} n
 * @return {number}
 */
var Fibonacci = function(n) {
  if (n == 0) {
      return 0; 
  } else if (n == 1) {
      return 1; 
  } else {
      return Fibonacci(n - 1) + Fibonacci(n - 2); 
  }
};
var fib = function(n) {
    return Fibonacci(n);
};

// TC: O(2^N); SC: O(N)

// end 